from typing import Dict, Any, List
import httpx
import random
from datetime import datetime, timedelta

class GSTEcosystem:
    def __init__(self, client: httpx.Client, api_key: str = None):
        self.client = client
        self.api_key = api_key
        self.token_supply = 1000000  # 1M GST tokens
        self.circulating_supply = 500000  # 500K em circulação
    
    def transfer_gst(self, from_user: str, to_user: str, amount: float) -> Dict[str, Any]:
        """Transferir tokens GST entre usuários"""
        transaction_id = f"GST_TXN_{random.randint(100000, 999999)}"
        
        return {
            "transaction_id": transaction_id,
            "from_user": from_user,
            "to_user": to_user,
            "amount": amount,
            "fee": amount * 0.01,  # 1% fee
            "status": "confirmed",
            "timestamp": datetime.utcnow().isoformat()
        }
    
    def reward_esg_activity(self, user_id: str, activity_type: str, esg_score: float) -> Dict[str, Any]:
        """Recompensar atividade ESG com tokens GST"""
        base_reward = 10.0
        esg_multiplier = esg_score / 100.0
        reward_amount = base_reward * esg_multiplier
        
        return {
            "user_id": user_id,
            "activity_type": activity_type,
            "esg_score": esg_score,
            "reward_amount": reward_amount,
            "gst_tokens_earned": int(reward_amount),
            "timestamp": datetime.utcnow().isoformat()
        }
    
    def create_esg_challenge(self, challenge_data: Dict[str, Any]) -> Dict[str, Any]:
        """Criar desafio ESG com recompensas GST"""
        challenge_id = f"CHALLENGE_{random.randint(100000, 999999)}"
        
        return {
            "challenge_id": challenge_id,
            "title": challenge_data.get("title", "ESG Challenge"),
            "description": challenge_data.get("description", "Complete sustainable activities"),
            "reward_gst": challenge_data.get("reward_gst", 100),
            "duration_days": challenge_data.get("duration_days", 7),
            "participants": 0,
            "status": "active",
            "created_at": datetime.utcnow().isoformat()
        }
    
    def join_esg_challenge(self, user_id: str, challenge_id: str) -> Dict[str, Any]:
        """Participar de desafio ESG"""
        return {
            "user_id": user_id,
            "challenge_id": challenge_id,
            "joined_at": datetime.utcnow().isoformat(),
            "progress": 0,
            "status": "active"
        }
    
    def complete_esg_challenge(self, user_id: str, challenge_id: str) -> Dict[str, Any]:
        """Completar desafio ESG e receber recompensas"""
        reward_gst = random.randint(50, 200)
        
        return {
            "user_id": user_id,
            "challenge_id": challenge_id,
            "completed_at": datetime.utcnow().isoformat(),
            "reward_gst": reward_gst,
            "status": "completed"
        }
    
    def get_user_gst_balance(self, user_id: str) -> Dict[str, Any]:
        """Obter saldo GST do usuário"""
        balance = random.randint(100, 5000)
        
        return {
            "user_id": user_id,
            "gst_balance": balance,
            "esg_level": self._calculate_esg_level(balance),
            "total_earned": balance + random.randint(500, 2000),
            "total_spent": random.randint(100, 1000)
        }
    
    def get_leaderboard(self, period: str = "monthly") -> Dict[str, Any]:
        """Obter ranking GST por período"""
        leaderboard = []
        for i in range(1, 11):
            leaderboard.append({
                "position": i,
                "user_id": f"user_{i}",
                "gst_balance": random.randint(1000, 10000),
                "esg_level": self._calculate_esg_level(random.randint(1000, 10000)),
                "monthly_earned": random.randint(100, 1000)
            })
        
        return {
            "period": period,
            "leaderboard": leaderboard,
            "total_participants": random.randint(100, 1000),
            "updated_at": datetime.utcnow().isoformat()
        }
    
    def _calculate_esg_level(self, gst_balance: float) -> str:
        """Calcular nível ESG baseado no saldo GST"""
        if gst_balance >= 5000:
            return "Mestre ESG"
        elif gst_balance >= 2000:
            return "Guardião Verde"
        elif gst_balance >= 1000:
            return "Intermediário ESG"
        elif gst_balance >= 500:
            return "Iniciante ESG"
        else:
            return "Novato ESG"
    
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "active",
            "module": "gst_ecosystem",
            "token_supply": self.token_supply,
            "circulating_supply": self.circulating_supply
        }
