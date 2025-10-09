"""
Exemplo de uso do ESG Asset Token - Estratégia Inteligente
"""

from guardflow_sdk import GuardFlowSDK

def main():
    # Inicializar SDK
    sdk = GuardFlowSDK(api_key="your-api-key")
    
    # Dados da nota fiscal
    invoice_data = {
        "invoice_number": "NF-2025-001234",
        "amount": 2000.00,
        "date": "2025-01-26",
        "products": [
            {
                "name": "Produto Orgânico Premium",
                "category": "Alimentos Orgânicos",
                "sustainable": True,
                "price": 100.00
            },
            {
                "name": "Energia Solar Residencial",
                "category": "Energia Renovável", 
                "sustainable": True,
                "price": 500.00
            },
            {
                "name": "Produto Sustentável",
                "category": "Eco-Friendly",
                "sustainable": True,
                "price": 200.00
            }
        ],
        "esg_value": 400.00,
        "carbon_offset_kg": 25.0
    }
    
    print("🔄 Convertendo nota fiscal em ESG Asset...")
    
    # Converter nota fiscal em ESG Asset
    asset_result = sdk.esg_asset.mint_from_invoice(invoice_data)
    
    print(f"✅ ESG Asset criado com sucesso!")
    print(f"🆔 Asset ID: {asset_result['asset_id']}")
    print(f"🌱 Score ESG: {asset_result['esg_score']:.1f}")
    print(f"💰 Valor fiscal: R$ {asset_result['fiscal_value']:,.2f}")
    print(f"🏛️ Créditos fiscais: {len(asset_result['tax_credits_available'])}")
    print(f"⛓️ Blockchain: {asset_result['transaction_hash']}")
    print(f"🔒 Imutável: {asset_result['immutable']}")
    
    # Staking para rendimento
    print("\n💰 Fazendo staking do ESG Asset...")
    staking_result = sdk.esg_asset.stake_for_rewards(
        asset_id=asset_result['asset_id'],
        amount=1000.0,
        duration_days=90
    )
    
    print(f"✅ Staking ativo!")
    print(f"🆔 Staking ID: {staking_result['staking_id']}")
    print(f"💰 Valor staked: R$ {staking_result['amount_staked']:,.2f}")
    print(f"📈 APY: {staking_result['apy']:.1f}%")
    print(f"🌱 Bônus ESG: {staking_result['esg_bonus_apy']:.1f}%")
    print(f"💎 Recompensa esperada: R$ {staking_result['expected_reward']:,.2f}")
    
    # Governança ESG
    print("\n🗳️ Participando da governança ESG...")
    vote_result = sdk.esg_asset.vote_on_proposal(
        asset_id=asset_result['asset_id'],
        proposal_id="PROP_001",
        vote="YES"
    )
    
    print(f"✅ Voto registrado!")
    print(f"🆔 Vote ID: {vote_result['vote_id']}")
    print(f"🗳️ Voto: {vote_result['vote']}")
    print(f"⚡ Poder de voto: {vote_result['voting_power']:.2f}")
    print(f"🌱 Score ESG: {vote_result['esg_score']:.1f}")
    print(f"💎 Recompensa: R$ {vote_result['reward_earned']:.2f}")
    
    # Opções de monetização
    print("\n💸 Analisando opções de monetização...")
    monetization = sdk.esg_asset.get_monetization_options(asset_result['asset_id'])
    
    print(f"📊 Score ESG: {monetization['esg_score']:.1f}")
    print(f"💰 Valor total potencial: R$ {monetization['total_potential_value']:,.2f}")
    
    print("\n💎 Opções de monetização:")
    for option_type, option_data in monetization['monetization_options'].items():
        print(f"  {option_data['description']}: R$ {option_data['amount']:,.2f}")
    
    # Comparação com NFT tradicional
    print("\n🆚 Comparação: ESG Asset vs NFT Tradicional")
    print("=" * 50)
    print("ESG Asset (Estratégia Inteligente):")
    print("✅ Registro imutável na blockchain")
    print("✅ Tokenização ESG com valor real")
    print("✅ Staking para rendimento passivo")
    print("✅ Governança com poder de voto")
    print("✅ Monetização de créditos fiscais")
    print("✅ Trading de créditos de carbono")
    print("✅ Múltiplas fontes de receita")
    
    print("\nNFT Tradicional:")
    print("❌ Apenas colecionabilidade")
    print("❌ Sem valor fiscal/legal")
    print("❌ Dependência de marketplaces")
    print("❌ Foco apenas em especulação")

if __name__ == "__main__":
    main()
