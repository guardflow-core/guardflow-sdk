from typing import Dict, Any, List, Optional
import httpx
import random
import hashlib
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import io
import base64

class InvoiceNFT:
    """
    Sistema de conversão de notas fiscais em NFTs ESG
    Cada nota fiscal vira um NFT único com metadados ESG
    """
    
    def __init__(self, client: httpx.Client, api_key: str = None):
        self.client = client
        self.api_key = api_key
        self.nft_contract_address = "0xGuardFlowNFT"
        self.metadata_base_uri = "https://metadata.guardflow.com/nft/"
    
    def convert_invoice_to_nft(self, invoice_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Converter nota fiscal em NFT ESG
        """
        # Gerar hash único da nota fiscal
        invoice_hash = self._generate_invoice_hash(invoice_data)
        
        # Calcular score ESG da nota
        esg_score = self._calculate_invoice_esg_score(invoice_data)
        
        # Gerar metadados do NFT
        nft_metadata = self._generate_nft_metadata(invoice_data, esg_score, invoice_hash)
        
        # Criar imagem do NFT
        nft_image = self._generate_nft_image(invoice_data, esg_score)
        
        # Mintar NFT na blockchain
        nft_result = self._mint_nft_on_blockchain(invoice_hash, nft_metadata, nft_image)
        
        return {
            "nft_id": nft_result["token_id"],
            "invoice_hash": invoice_hash,
            "esg_score": esg_score,
            "nft_metadata": nft_metadata,
            "image_url": nft_result["image_url"],
            "blockchain_tx": nft_result["transaction_hash"],
            "rarity": self._calculate_nft_rarity(esg_score),
            "created_at": datetime.utcnow().isoformat()
        }
    
    def _generate_invoice_hash(self, invoice_data: Dict[str, Any]) -> str:
        """Gerar hash único da nota fiscal"""
        invoice_string = f"{invoice_data.get('invoice_number', '')}{invoice_data.get('amount', 0)}{invoice_data.get('date', '')}"
        return hashlib.sha256(invoice_string.encode()).hexdigest()[:16]
    
    def _calculate_invoice_esg_score(self, invoice_data: Dict[str, Any]) -> float:
        """Calcular score ESG da nota fiscal"""
        base_score = 50.0
        
        # Bônus por produtos sustentáveis
        products = invoice_data.get("products", [])
        sustainable_bonus = 0
        for product in products:
            if product.get("sustainable", False):
                sustainable_bonus += 10
        
        # Bônus por valor ESG
        esg_value = invoice_data.get("esg_value", 0)
        value_bonus = min(esg_value / 100, 20)  # Máximo 20 pontos
        
        # Bônus por categoria ESG
        category_bonus = 0
        for product in products:
            category = product.get("category", "").lower()
            if any(keyword in category for keyword in ["orgânico", "sustentável", "eco", "verde"]):
                category_bonus += 5
        
        total_score = base_score + sustainable_bonus + value_bonus + category_bonus
        return min(total_score, 100.0)
    
    def _generate_nft_metadata(self, invoice_data: Dict[str, Any], esg_score: float, invoice_hash: str) -> Dict[str, Any]:
        """Gerar metadados do NFT"""
        rarity = self._calculate_nft_rarity(esg_score)
        
        return {
            "name": f"GuardFlow ESG Invoice #{invoice_hash[:8]}",
            "description": f"Nota fiscal ESG tokenizada com score {esg_score:.1f}",
            "image": f"{self.metadata_base_uri}{invoice_hash}.png",
            "attributes": [
                {
                    "trait_type": "ESG Score",
                    "value": esg_score,
                    "max_value": 100
                },
                {
                    "trait_type": "Rarity",
                    "value": rarity
                },
                {
                    "trait_type": "Invoice Amount",
                    "value": invoice_data.get("amount", 0)
                },
                {
                    "trait_type": "Sustainable Products",
                    "value": len([p for p in invoice_data.get("products", []) if p.get("sustainable", False)])
                },
                {
                    "trait_type": "Carbon Offset",
                    "value": invoice_data.get("carbon_offset_kg", 0)
                },
                {
                    "trait_type": "Tokenization Date",
                    "value": datetime.utcnow().strftime("%Y-%m-%d")
                }
            ],
            "external_url": f"https://guardflow.com/nft/{invoice_hash}",
            "background_color": self._get_background_color(esg_score)
        }
    
    def _generate_nft_image(self, invoice_data: Dict[str, Any], esg_score: float) -> str:
        """Gerar imagem do NFT"""
        # Criar imagem base
        img = Image.new('RGB', (512, 512), color=self._get_background_color(esg_score))
        draw = ImageDraw.Draw(img)
        
        # Adicionar elementos visuais
        self._draw_nft_elements(draw, invoice_data, esg_score)
        
        # Converter para base64
        img_buffer = io.BytesIO()
        img.save(img_buffer, format='PNG')
        img_base64 = base64.b64encode(img_buffer.getvalue()).decode()
        
        return f"data:image/png;base64,{img_base64}"
    
    def _draw_nft_elements(self, draw: ImageDraw.Draw, invoice_data: Dict[str, Any], esg_score: float):
        """Desenhar elementos visuais do NFT"""
        # Título
        draw.text((50, 50), "GuardFlow ESG Invoice", fill="white", font_size=24)
        
        # Score ESG
        draw.text((50, 100), f"ESG Score: {esg_score:.1f}", fill="white", font_size=20)
        
        # Valor
        amount = invoice_data.get("amount", 0)
        draw.text((50, 130), f"Amount: R$ {amount:,.2f}", fill="white", font_size=16)
        
        # Produtos sustentáveis
        sustainable_count = len([p for p in invoice_data.get("products", []) if p.get("sustainable", False)])
        draw.text((50, 160), f"Sustainable Products: {sustainable_count}", fill="white", font_size=16)
        
        # Data
        draw.text((50, 190), f"Date: {datetime.utcnow().strftime('%Y-%m-%d')}", fill="white", font_size=16)
        
        # Elementos decorativos baseados no score ESG
        if esg_score >= 80:
            # Desenhar folhas verdes
            for i in range(5):
                x = 400 + i * 20
                y = 200 + i * 10
                draw.ellipse([x, y, x+20, y+20], fill="green")
        elif esg_score >= 60:
            # Desenhar círculos
            for i in range(3):
                x = 400 + i * 30
                y = 250
                draw.ellipse([x, y, x+15, y+15], fill="lightgreen")
    
    def _get_background_color(self, esg_score: float) -> str:
        """Obter cor de fundo baseada no score ESG"""
        if esg_score >= 90:
            return "#1B5E20"  # Verde escuro
        elif esg_score >= 80:
            return "#2E7D32"  # Verde
        elif esg_score >= 70:
            return "#388E3C"  # Verde médio
        elif esg_score >= 60:
            return "#4CAF50"  # Verde claro
        else:
            return "#8BC34A"  # Verde claro
    
    def _calculate_nft_rarity(self, esg_score: float) -> str:
        """Calcular raridade do NFT baseada no score ESG"""
        if esg_score >= 95:
            return "Legendary"
        elif esg_score >= 90:
            return "Epic"
        elif esg_score >= 80:
            return "Rare"
        elif esg_score >= 70:
            return "Uncommon"
        else:
            return "Common"
    
    def _mint_nft_on_blockchain(self, invoice_hash: str, metadata: Dict[str, Any], image: str) -> Dict[str, Any]:
        """Mintar NFT na blockchain"""
        # Mock blockchain transaction
        token_id = f"GFNFT_{random.randint(100000, 999999)}"
        transaction_hash = f"0x{random.randint(100000, 999999)}"
        
        return {
            "token_id": token_id,
            "transaction_hash": transaction_hash,
            "image_url": f"{self.metadata_base_uri}{invoice_hash}.png",
            "gas_used": random.randint(50000, 100000),
            "gas_price": 0.00002
        }
    
    def get_nft_collection(self, user_id: str) -> Dict[str, Any]:
        """Obter coleção de NFTs do usuário"""
        # Mock collection data
        nfts = []
        for i in range(random.randint(3, 10)):
            nfts.append({
                "nft_id": f"GFNFT_{random.randint(100000, 999999)}",
                "invoice_hash": f"INV_{random.randint(100000, 999999)}",
                "esg_score": random.uniform(60, 95),
                "rarity": random.choice(["Common", "Uncommon", "Rare", "Epic", "Legendary"]),
                "created_at": datetime.utcnow().isoformat(),
                "image_url": f"https://metadata.guardflow.com/nft/{random.randint(100000, 999999)}.png"
            })
        
        return {
            "user_id": user_id,
            "total_nfts": len(nfts),
            "nfts": nfts,
            "total_esg_score": sum(nft["esg_score"] for nft in nfts),
            "average_esg_score": sum(nft["esg_score"] for nft in nfts) / len(nfts) if nfts else 0
        }
    
    def trade_nft(self, from_user: str, to_user: str, nft_id: str, price_gst: float) -> Dict[str, Any]:
        """Negociar NFT por tokens GST"""
        return {
            "trade_id": f"TRADE_{random.randint(100000, 999999)}",
            "nft_id": nft_id,
            "from_user": from_user,
            "to_user": to_user,
            "price_gst": price_gst,
            "status": "completed",
            "traded_at": datetime.utcnow().isoformat()
        }
    
    def get_nft_marketplace(self) -> Dict[str, Any]:
        """Obter marketplace de NFTs"""
        # Mock marketplace data
        listings = []
        for i in range(random.randint(10, 50)):
            listings.append({
                "nft_id": f"GFNFT_{random.randint(100000, 999999)}",
                "seller": f"user_{random.randint(1, 100)}",
                "price_gst": random.randint(100, 5000),
                "esg_score": random.uniform(60, 95),
                "rarity": random.choice(["Common", "Uncommon", "Rare", "Epic", "Legendary"]),
                "listed_at": datetime.utcnow().isoformat()
            })
        
        return {
            "total_listings": len(listings),
            "listings": listings,
            "floor_price": min(listing["price_gst"] for listing in listings) if listings else 0,
            "average_price": sum(listing["price_gst"] for listing in listings) / len(listings) if listings else 0
        }
    
    def get_status(self) -> Dict[str, Any]:
        return {"status": "active", "module": "invoice_nft"}
