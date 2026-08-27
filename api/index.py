# ================================================================
# api/index.py — Vercel Serverless Handler
# ================================================================
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from datetime import datetime
from src.config import Config
from src.spammer import OTPSpammer

def handler(request):
    """
    Fungsi utama untuk Vercel serverless
    """
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type",
        "Content-Type": "application/json"
    }
    
    if request.method == "OPTIONS":
        return {"statusCode": 200, "headers": headers, "body": ""}
    
    if request.method == "GET":
        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps({
                "status": "online",
                "bot": "MySPAMBot-OTP MAX",
                "version": "3.0",
                "features": {
                    "max_threads": Config.MAX_THREADS,
                    "max_amount": Config.MAX_AMOUNT,
                    "endpoints": 100,
                    "parallel": True,
                    "proxy": Config.USE_PROXY
                },
                "timestamp": datetime.now().isoformat()
            }, indent=2)
        }
    
    if request.method == "POST":
        try:
            body = json.loads(request.body or "{}")
            
            target = body.get("target", "").strip()
            amount = int(body.get("amount", 100))
            threads = int(body.get("threads", Config.MAX_THREADS))
            
            if not target:
                return {
                    "statusCode": 400,
                    "headers": headers,
                    "body": json.dumps({"success": False, "message": "Parameter 'target' wajib diisi!"})
                }
            
            spammer = OTPSpammer()
            result = spammer.run_spam_parallel(target, amount, threads)
            
            return {
                "statusCode": 200,
                "headers": headers,
                "body": json.dumps({
                    "success": True,
                    "target": target,
                    "total": result["total"],
                    "sent": result["success"],
                    "failed": result["failed"],
                    "success_rate": result["success_rate"],
                    "speed": result["speed"],
                    "duration": result["duration"],
                    "preview": result["results"][:10],
                    "timestamp": datetime.now().isoformat()
                }, indent=2)
            }
            
        except Exception as e:
            return {
                "statusCode": 500,
                "headers": headers,
                "body": json.dumps({"success": False, "error": str(e)[:200]})
            }
    
    return {"statusCode": 405, "headers": headers, "body": "Method not allowed"}
