# ================================================================
# src/config.py — Konfigurasi
# ================================================================

class Config:
    # Untuk Vercel
    MAX_THREADS = 50
    MAX_AMOUNT = 1000
    TIMEOUT = 5
    MAX_RETRY = 3
    
    # Untuk CLI
    MIN_DELAY = 0.1
    MAX_DELAY = 0.5
    USE_PROXY = False
    PROXY_LIST = []
