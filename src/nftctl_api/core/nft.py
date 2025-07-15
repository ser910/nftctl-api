import subprocess
from nftctl_api.models.firewall import Rule

def list_rules():
    result = subprocess.run(["nft", "list", "ruleset"], capture_output=True, text=True)
    return result.stdout

def apply_rule(rule: Rule):
    cmd = [
        "nft", "add", "rule", "inet", "filter", rule.chain,
        rule.proto, "dport", str(rule.dport), rule.action
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(result.stderr)
    return result.stdout
