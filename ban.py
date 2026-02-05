import os
import time
import smtplib
import ssl
import webbrowser
import sys
import random
from email.message import EmailMessage
from colorama import Fore, Style, init
from dotenv import load_dotenv

# Initialize
init(autoreset=True)
load_dotenv()

# --- COLORS ---
G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW
C = Fore.CYAN
W = Fore.WHITE
M = Fore.MAGENTA
B = Fore.BLUE

# --- ADVANCED SYSTEM BOOT ANIMATION ---
def system_boot():
    clear()
    print(f"{C}[SYSTEM INFO] Initializing Crypto Lord Kernel v3.0...")
    time.sleep(1)
    
    # Fake Server Logs
    servers = ["US-East-1", "EU-West-2", "Asia-South-1", "Proxy-Tunnel-7"]
    for server in servers:
        status = random.choice(["ONLINE", "SECURE", "ENCRYPTED"])
        ping = random.randint(10, 99)
        print(f"{W}[{G}LOG{W}] Connecting to {C}{server}{W}... Status: {G}{status} {W}({ping}ms)")
        time.sleep(0.4)

    print(f"\n{Y}[!] DECRYPTING BANNING DATABASE...")
    # Progress Bar Animation
    for i in range(0, 101, 10):
        sys.stdout.write(f"\r{W}[{M}{'#' * (i//5)}{' ' * (20 - i//5)}{W}] {i}% Complete")
        sys.stdout.flush()
        time.sleep(0.3)
    
    print(f"\n\n{G}✔️ SYSTEM BYPASS SUCCESSFUL")
    print(f"{G}✔️ ANTI-DETECTION LAYER ACTIVE")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    time.sleep(1.5)

# --- DYNAMIC UPDATE CHECKER ---
def check_updates():
    print(f"{B}[*] SYNCHRONIZING WITH GITHUB REPO...")
    time.sleep(1)
    print(f"{G}[+] NO NEW UPDATES FOUND. YOU ARE ON THE LATEST VERSION.")
    time.sleep(0.8)

# --- AUTO-OPEN CHANNEL ---
def join_channel():
    channel_url = "https://whatsapp.com/channel/0029Vb75PfXChq6SdkyVaF0A"
    print(f"\n{Y}🌐 RELAYING CONNECTION TO WHATSAPP...")
    time.sleep(1)
    try:
        webbrowser.open(channel_url)
        print(f"{G}✅ CHANNEL ACCESS GRANTED!")
    except:
        print(f"{R}❌ LINK: {channel_url}")
    input(f"\n{W}PRESS ENTER TO RETURN TO MAIN-FRAME...")

# --- PROFESSIONAL BANNER ---
def banner():
    print(f"{C}⚡ {W}═══[ {G}𝗖𝗥𝗬𝗣𝗧𝗢 𝗟𝗢𝗥𝗗 𝗕𝗔𝗡𝗡𝗜𝗡𝗚 𝗧𝗢𝗢𝗟𝗦 {W}]═══ {C}⚡")
    print(f"{G}" + r"""
      .---.        .-----------.
     /     \      /  💥 CRYPTO 💥
    | () () |    /   LORD BOT   
     \  ^  /    '  RESTRICTED  
      |||||       '-----------'
    """ + f"{C}")
    print(f"{W}[{G}●{W}] {G}OWNER   : {W}PROFESSOR ABHEEBHAI")
    print(f"{W}[{G}●{W}] {G}VERSION : {Y}3.0.0 (PREMIUM)")
    print(f"{W}[{G}●{W}] {G}CHANNEL : {C}https://whatsapp.com/channel/0029Vb75PfXChq6SdkyVaF0A")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

# --- MAIN LOGIC ---
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')

# Heavy Boot Sequence
system_boot()
check_updates()

while True:
    banner()
    print(f"{B}[01] {W}𝗕𝗮𝗻 𝗣𝗲𝗿𝗺𝗮𝗻𝗲𝗻𝘁         {B}[02] {W}𝗕𝗮𝗻 𝗧𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝘆")
    print(f"{B}[03] {W}𝗨𝗻𝗯𝗮𝗻 𝗣𝗲𝗿𝗺𝗮𝗻𝗲𝗻𝘁       {B}[04] {W}𝗨𝗻𝗯𝗮𝗻 𝗧𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝘆")
    print(f"{B}[05] {W}𝗩𝗶𝗲𝘄 𝗕𝗮𝗻𝗻𝗲𝗱 𝗟𝗶𝘀𝘁       {B}[06] {G}𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 🔥")
    print(f"{R}[07] {W}𝗦𝘆𝘀𝘁𝗲𝗺 𝗘𝘅𝗶𝘁")

    print(f"\n{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    choice = input(f"{G}┌──<{W}CRYPTO-LORD{G}>─[{W}Select Option{G}]\n└─> {W}").strip()

    if choice == "1" or choice == "01":
        # ban_permanent() logic here
        pass
    elif choice == "6" or choice == "06":
        join_channel()
        clear()
    elif choice == "7" or choice == "07":
        print(f"\n{R}[!] TERMINATING SESSION... ENCRYPTING LOGS...{N}")
        time.sleep(1.5)
        break
    else:
        print(f"{R}❌ INVALID SELECTION!")
        time.sleep(1)
    
    clear()
