from pydantic import BaseModel

class Rule(BaseModel):
    chain: str
    proto: str
    dport: int
    action: str
