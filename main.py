# ================================================================
# main.py — Entry Point untuk CLI
# ================================================================

import sys
from src.cli import autoketik, start, hijau, putih, merah

if __name__ == "__main__":
    autoketik(f"""
{hijau}╔══════════════════════════════════════════════════════════════════╗
║          MySPAMBot-OTP — MAXIMUM SPAM ENGINE                  ║
║                          v3.0                                 ║
╠══════════════════════════════════════════════════════════════════╣
║  📌 Fitur:                                                     ║
║  • 100+ Endpoint OTP                                           ║
║  • Multi-threading (paralel)                                   ║
║  • Auto retry & proxy                                          ║
║  • User-agent rotation                                         ║
╚══════════════════════════════════════════════════════════════════╝
    """)
    
    nomor = input(f"{putih}Masukkan nomor target: {hijau}")
    if not nomor:
        autoketik(f"{merah}Nomor tidak boleh kosong!")
        sys.exit()
    
    start(nomor, 1)
