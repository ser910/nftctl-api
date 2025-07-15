# nftctl-api

**nftctl-api** is a RESTful backend service written in Python using FastAPI, designed to manage Linux firewall rules via `nftables`.

This project aims to be a modular, extensible replacement backend for OPNsense-style systems on Linux, replacing `pf` and FreeBSD dependencies with `nftables` and Python.

---

## 🚀 Features

- Manage `nftables` rules via HTTP API
- Add/remove basic firewall rules
- List active ruleset
- Modular structure ready for:
  - NAT, port forwarding
  - Interface management
  - WireGuard, DHCP, DNS services
- Designed for integration with external UI (forced from OPENSENSE)


