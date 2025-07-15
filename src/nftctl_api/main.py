from fastapi import FastAPI
from nftctl_api.api import firewall

app = FastAPI(title="nftctl API", version="0.1")

app.include_router(firewall.router, prefix="/api/firewall")
