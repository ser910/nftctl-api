from fastapi import APIRouter
from nftctl_api.models.firewall import Rule
from nftctl_api.core.nft import apply_rule, list_rules

router = APIRouter()

@router.get("/rules")
def get_rules():
    return {"rules": list_rules()}

@router.post("/rules")
def post_rule(rule: Rule):
    return {"result": apply_rule(rule)}
