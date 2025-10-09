"""
Exemplo de uso do sistema de NFTs de notas fiscais ESG
"""

from guardflow_sdk import GuardFlowSDK

def main():
    # Inicializar SDK
    sdk = GuardFlowSDK(api_key="your-api-key")
    
    # Dados da nota fiscal
    invoice_data = {
        "invoice_number": "NF-2025-001234",
        "amount": 1500.00,
        "date": "2025-01-26",
        "products": [
            {
                "name": "Produto Orgânico Premium",
                "category": "Alimentos Orgânicos",
                "sustainable": True,
                "price": 50.00
            },
            {
                "name": "Energia Solar Residencial",
                "category": "Energia Renovável",
                "sustainable": True,
                "price": 200.00
            },
            {
                "name": "Produto Convencional",
                "category": "Alimentos",
                "sustainable": False,
                "price": 30.00
            }
        ],
        "esg_value": 250.00,
        "carbon_offset_kg": 15.5
    }
    
    print("🔄 Convertendo nota fiscal em NFT ESG...")
    
    # Converter nota fiscal em NFT
    nft_result = sdk.nft.convert_invoice_to_nft(invoice_data)
    
    print(f"✅ NFT criado com sucesso!")
    print(f"📄 NFT ID: {nft_result['nft_id']}")
    print(f"🌱 Score ESG: {nft_result['esg_score']:.1f}")
    print(f"⭐ Raridade: {nft_result['rarity']}")
    print(f"🔗 Hash da nota: {nft_result['invoice_hash']}")
    print(f"🖼️ Imagem: {nft_result['image_url']}")
    print(f"⛓️ Transação blockchain: {nft_result['blockchain_tx']}")
    
    # Obter coleção do usuário
    print("\n📚 Obtendo coleção de NFTs do usuário...")
    collection = sdk.nft.get_nft_collection("user-123")
    
    print(f"📊 Total de NFTs: {collection['total_nfts']}")
    print(f"🌱 Score ESG médio: {collection['average_esg_score']:.1f}")
    print(f"📈 Score ESG total: {collection['total_esg_score']:.1f}")
    
    # Marketplace de NFTs
    print("\n🏪 Acessando marketplace de NFTs...")
    marketplace = sdk.nft.get_nft_marketplace()
    
    print(f"📦 Total de listagens: {marketplace['total_listings']}")
    print(f"💰 Preço mínimo: {marketplace['floor_price']} GST")
    print(f"📊 Preço médio: {marketplace['average_price']:.2f} GST")
    
    # Negociar NFT
    print("\n💱 Negociando NFT...")
    trade_result = sdk.nft.trade_nft(
        from_user="user-123",
        to_user="user-456", 
        nft_id=nft_result['nft_id'],
        price_gst=500.0
    )
    
    print(f"✅ Negociação realizada!")
    print(f"🆔 Trade ID: {trade_result['trade_id']}")
    print(f"💰 Preço: {trade_result['price_gst']} GST")
    print(f"👤 Vendedor: {trade_result['from_user']}")
    print(f"👤 Comprador: {trade_result['to_user']}")

if __name__ == "__main__":
    main()
