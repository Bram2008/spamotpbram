# ================================================================
# src/cli.py — Fungsi CLI (autoketik, countdown, tanya, start)
# ================================================================

import sys
import time
from src.spammer import OTPSpammer

# Warna terminal
hijau   = "\033[1;92m"
putih   = "\033[1;97m"
abu     = "\033[1;90m"
kuning  = "\033[1;93m"
ungu    = "\033[1;95m"
merah   = "\033[1;91m"
biru    = "\033[1;96m"

def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.050)

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = f'\033[1;97m[\033[1;93m•\033[1;97m] Silakan Menunggu Dalam Waktu \033[1;92m{mins:02d}:{secs:02d}'
        waktu = time.localtime()
        print(f"{timeformat} | {biru}{time.strftime('%A, %d %B %Y', waktu)} | {kuning}Waktu {time.strftime('%H:%M:%S', waktu)}", end='\r')
        time.sleep(1)
        time_sec -= 1

def tanya(nomor):
    while True:
        a = input(f"{merah}Apakah Anda ingin mengulangi Spam Tools? y/t \n{putih}Input Anda: {hijau}")
        if a.lower() == "y":
            start(nomor, 1)
            break
        elif a.lower() == "t":
            autoketik(f"{hijau}Berhasil Keluar Dari Tools")
            sys.exit()
        else:
            print("Masukkan Pilihan Dengan Benar")

def start(nomor, mode=0):
    """Fungsi utama untuk CLI mode"""
    autoketik(f"""
{hijau}╔══════════════════════════════════════════════════════════════════╗
║          MySPAMBot-OTP — MAXIMUM SPAM ENGINE                  ║
║                          v3.0                                 ║
╚══════════════════════════════════════════════════════════════════╝
    """)
    
    autoketik(f"{hijau}📱 Target: {nomor}")
    autoketik(f"{hijau}⚡ Mode: {'Parallel' if mode == 1 else 'Sequential'}")
    
    if mode == 1:
        # Mode parallel (multi-thread)
        amount = 100
        threads = 50
        autoketik(f"{hijau}📊 Jumlah: {amount} OTP")
        autoketik(f"{hijau}🔧 Thread: {threads}")
        
        spammer = OTPSpammer()
        result = spammer.run_spam_parallel(nomor, amount, threads)
        
        autoketik(f"""
{hijau}╔══════════════════════════════════════════════════════════════════╗
║                    HASIL SPAM                                       ║
╠══════════════════════════════════════════════════════════════════╣
║  Total      : {result['total']}                                    ║
║  Berhasil   : {result['success']} ✅                               ║
║  Gagal      : {result['failed']} ❌                               ║
║  Rate       : {result['success_rate']}                             ║
║  Kecepatan  : {result['speed']}                                    ║
║  Durasi     : {result['duration']}                                 ║
╚══════════════════════════════════════════════════════════════════╝
        """)
    else:
        # Mode sequential
        autoketik(f"{kuning}Mode sequential (1 thread)...")
        for i in range(10):
            autoketik(f"{hijau}Mengirim OTP ke {nomor} ({i+1}/10)")
            time.sleep(1)
    
    tanya(nomor)
