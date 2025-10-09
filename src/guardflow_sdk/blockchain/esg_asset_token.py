from typing import Dict, Any, List, Optional
import httpx
import random
import hashlib
from datetime import datetime
from enum import Enum

class ESGValueType(Enum):
    """Tipos de valor ESG"""
    TOKENIZATION_REWARD = "tokenization_reward"
    STAKING_YIELD = "staking_yield"
    GOVERNANCE_REWARD = "governance_reward"
    TAX_CREDIT_MONETIZATION = "tax_credit_monetization"
    CARBON_CREDIT_TRADING = "carbon_credit_trading"

class ESGInvoiceAsset:
    """
    Asset ESG imutável baseado em notas fiscais
    Combina registro imutável + tokenização + staking + governança
    """
    
    def __init__(self, client: httpx.Client, api_key: str = None):
        self.client = client
        self.api_key = api_key
        self.contract_address = "0xGuardFlowESG"
        self.staking_pools = {}
        self.governance_proposals = {}
    
    def mint_from_invoice(self, invoice_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Converter nota fiscal em ESG Asset imutável
        """
        # Gerar hash único da nota fiscal
        invoice_hash = self._generate_invoice_hash(invoice_data)
        
        # Calcular score ESG
        esg_score = self._calculate_esg_score(invoice_data)
        
        # Calcular valor fiscal
        fiscal_value = invoice_data.get("amount", 0)
        
        # Identificar créditos fiscais disponíveis
        tax_credits = self._identify_tax_credits(invoice_data)
        
        # Criar asset ESG
        asset_id = f"ESG_ASSET_{random.randint(100000, 999999)}"
        
        asset_data = {
            "asset_id": asset_id,
            "invoice_hash": invoice_hash,
            "esg_score": esg_score,
            "sustainability_bonus": self._calculate_sustainability_bonus(invoice_data),
            "carbon_offset_kg": invoice_data.get("carbon_offset_kg", 0),
            "fiscal_value": fiscal_value,
            "tax_credits_available": tax_credits,
            "block_number": random.randint(1000000, 9999999),
            "transaction_hash": f"0x{random.randint(100000, 999999)}",
            "immutable": True,
            "staking_enabled": True,
            "governance_voting": True,
            "tradeable": True,
            "created_at": datetime.utcnow().isoformat()
        }
        
        return asset_data
    
    def stake_for_rewards(self, asset_id: str, amount: float, duration_days: int) -> Dict[str, Any]:
        """
        Staking de tokens ESG para rendimento
        """
        # Calcular APY baseado no score ESG
        esg_score = self._get_asset_esg_score(asset_id)
        base_apy = 8.0
        esg_bonus = (esg_score / 100.0) * 7.0  # Até 7% bônus
        total_apy = base_apy + esg_bonus
        
        # Calcular recompensas
        annual_reward = amount * (total_apy / 100.0)
        duration_reward = annual_reward * (duration_days / 365.0)
        
        staking_id = f"STAKE_{random.randint(100000, 999999)}"
        
        return {
            "staking_id": staking_id,
            "asset_id": asset_id,
            "amount_staked": amount,
            "duration_days": duration_days,
            "apy": total_apy,
            "expected_reward": duration_reward,
            "esg_bonus_apy": esg_bonus,
            "status": "active",
            "created_at": datetime.utcnow().isoformat(),
            "maturity_date": (datetime.utcnow().timestamp() + duration_days * 86400)
        }
    
    def vote_on_proposal(self, asset_id: str, proposal_id: str, vote: str) -> Dict[str, Any]:
        """
        Votar em propostas de governança ESG
        """
        # Calcular poder de voto baseado no score ESG
        esg_score = self._get_asset_esg_score(asset_id)
        voting_power = esg_score / 100.0  # 0.0 a 1.0
        
        vote_id = f"VOTE_{random.randint(100000, 999999)}"
        
        return {
            "vote_id": vote_id,
            "asset_id": asset_id,
            "proposal_id": proposal_id,
            "vote": vote,
            "voting_power": voting_power,
            "esg_score": esg_score,
            "reward_earned": voting_power * 10,  # Recompensa por participação
            "timestamp": datetime.utcnow().isoformat()
        }
    
    def get_monetization_options(self, asset_id: str) -> Dict[str, Any]:
        """
        Obter opções de monetização do asset ESG
        """
        esg_score = self._get_asset_esg_score(asset_id)
        fiscal_value = self._get_asset_fiscal_value(asset_id)
        
        # Tokenização ESG
        tokenization_reward = fiscal_value * 0.03  # 3% base
        
        # Staking yield
        staking_yield = fiscal_value * 0.08 * (esg_score / 100.0)  # 8% base com bônus ESG
        
        # Governança
        governance_reward = esg_score * 2  # R$ 2 por ponto ESG
        
        # Créditos fiscais
        tax_credits = self._calculate_tax_credits(fiscal_value)
        
        # Carbon credits
        carbon_credits = self._calculate_carbon_credits(asset_id)
        
        return {
            "asset_id": asset_id,
            "esg_score": esg_score,
            "monetization_options": {
                "tokenization_reward": {
                    "amount": tokenization_reward,
                    "type": ESGValueType.TOKENIZATION_REWARD.value,
                    "description": "Recompensa por tokenização ESG"
                },
                "staking_yield": {
                    "amount": staking_yield,
                    "type": ESGValueType.STAKING_YIELD.value,
                    "description": "Rendimento por staking ESG"
                },
                "governance_reward": {
                    "amount": governance_reward,
                    "type": ESGValueType.GOVERNANCE_REWARD.value,
                    "description": "Recompensa por participação em governança"
                },
                "tax_credits": {
                    "amount": tax_credits,
                    "type": ESGValueType.TAX_CREDIT_MONETIZATION.value,
                    "description": "Monetização de créditos fiscais"
                },
                "carbon_credits": {
                    "amount": carbon_credits,
                    "type": ESGValueType.CARBON_CREDIT_TRADING.value,
                    "description": "Trading de créditos de carbono"
                }
            },
            "total_potential_value": tokenization_reward + staking_yield + governance_reward + tax_credits + carbon_credits
        }
    
    def _generate_invoice_hash(self, invoice_data: Dict[str, Any]) -> str:
        """Gerar hash único da nota fiscal"""
        invoice_string = f"{invoice_data.get('invoice_number', '')}{invoice_data.get('amount', 0)}{invoice_data.get('date', '')}"
        return hashlib.sha256(invoice_string.encode()).hexdigest()[:16]
    
    def _calculate_esg_score(self, invoice_data: Dict[str, Any]) -> float:
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
        value_bonus = min(esg_value / 100, 20)
        
        # Bônus por categoria ESG
        category_bonus = 0
        for product in products:
            category = product.get("category", "").lower()
            if any(keyword in category for keyword in ["orgânico", "sustentável", "eco", "verde"]):
                category_bonus += 5
        
        total_score = base_score + sustainable_bonus + value_bonus + category_bonus
        return min(total_score, 100.0)
    
    def _calculate_sustainability_bonus(self, invoice_data: Dict[str, Any]) -> float:
        """Calcular bônus de sustentabilidade"""
        products = invoice_data.get("products", [])
        bonus = 0.0
        
        for product in products:
            if product.get("sustainable", False):
                bonus += 0.05  # 5% por produto sustentável
        
        return min(bonus, 0.20)  # Máximo 20%
    
    def _identify_tax_credits(self, invoice_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identificar créditos fiscais disponíveis"""
        amount = invoice_data.get("amount", 0)
        
        tax_credits = []
        
        # ICMS
        if amount > 100:
            tax_credits.append({
                "type": "ICMS",
                "rate": 0.18,
                "value": amount * 0.18,
                "processing_days": 45
            })
        
        # IPI
        if amount > 500:
            tax_credits.append({
                "type": "IPI", 
                "rate": 0.15,
                "value": amount * 0.15,
                "processing_days": 60
            })
        
        # PIS/COFINS
        if amount > 200:
            tax_credits.append({
                "type": "PIS_COFINS",
                "rate": 0.0365,
                "value": amount * 0.0365,
                "processing_days": 90
            })
        
        return tax_credits
    
    def _get_asset_esg_score(self, asset_id: str) -> float:
        """Obter score ESG do asset"""
        # Mock - em produção viria da blockchain
        return random.uniform(60, 95)
    
    def _get_asset_fiscal_value(self, asset_id: str) -> float:
        """Obter valor fiscal do asset"""
        # Mock - em produção viria da blockchain
        return random.uniform(100, 5000)
    
    def _calculate_tax_credits(self, fiscal_value: float) -> float:
        """Calcular valor dos créditos fiscais"""
        return fiscal_value * 0.15  # 15% médio
    
    def _calculate_carbon_credits(self, asset_id: str) -> float:
        """Calcular créditos de carbono"""
        # Mock - baseado no ESG score
        esg_score = self._get_asset_esg_score(asset_id)
        return esg_score * 0.5  # R$ 0.50 por ponto ESG
    
    def get_status(self) -> Dict[str, Any]:
        return {"status": "active", "module": "esg_asset_token"}
