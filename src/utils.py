# ================================================================
# src/utils.py — Proxy & User-Agent Manager
# ================================================================

import random
from src.config import Config

try:
    from fake_useragent import UserAgent
except ImportError:
    UserAgent = None

class ProxyManager:
    def __init__(self):
        self.proxies = Config.PROXY_LIST or [None]
        self.current_index = 0
    
    def get_proxy(self):
        if not Config.USE_PROXY:
            return None
        proxy = self.proxies[self.current_index % len(self.proxies)]
        self.current_index += 1
        return {"http": proxy, "https": proxy} if proxy else None


class UserAgentManager:
    def __init__(self):
        try:
            self.ua = UserAgent()
        except:
            self.ua = None
    
    def get_ua(self):
        if self.ua:
            return self.ua.random
        agents = [
            "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36",
            "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15"
        ]
        return random.choice(agents)
