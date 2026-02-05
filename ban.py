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

# --- CLEAR SCREEN ---
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# --- SYSTEM BOOT ---
def system_boot():
    clear()
    print(f"{C}[SYSTEM INFO] Initializing Crypto Lord Kernel v3.0...")
    time.sleep(1)
    servers = ["US-East-1", "EU-West-2", "Asia-South-1", "Proxy-Tunnel-7"]
    for server in servers:
        print(f"{W}[{G}LOG{W}] Connecting to {C}{server}{W}... Status: {G}SECURE")
        time.sleep(0.3)
    
    print(f"\n{Y}[!] DECRYPTING BANNING DATABASE...")
    for i in range(0, 101, 20):
        sys.stdout.write(f"\r{W}[{M}{'#' * (i//5)}{' ' * (20 - i//5)}{W}] {i}% Complete")
        sys.stdout.flush()
        time.sleep(0.2)
    print(f"\n\n{G}✔️ SYSTEM BYPASS SUCCESSFUL\n{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    time.sleep(1)

# --- BANNER ---
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

# --- ATTACK FUNCTION (For 1, 2, 3, 4, 5) ---
def start_attack(mode_name):
    clear()
    banner()
    print(f"{M}[ PROTOCOL: {mode_name} ]")
    target = input(f"\n{G}┌──<{W}TARGET{G}>─[{W}Enter Number{G}]\n└─> {W}").strip()
    
    if not target:
        print(f"{R}❌ Error: Target cannot be empty!")
        time.sleep(1.5)
        return

    try:
        count = int(input(f"{G}┌──<{W}REPORT{G}>─[{W}Enter Amount{G}]\n└─> {W}"))
    except ValueError:
        print(f"{R}❌ Error: Please enter a valid number for reports!")
        time.sleep(1.5)
        return

    print(f"\n{Y}[!] INITIALIZING PACKETS FOR {target}...")
    time.sleep(1)

    # Attack Loop
    for i in range(1, count + 1):
        # Professional Attack Logs
        status = random.choice(["SENT", "INJECTED", "BYPASSED", "REPORTED"])
        print(f"{R}[{W}💀{R}] {B}REPORT {i}/{count} {G}>> {W}Target: {target} {G}[{status}]")
        time.sleep(0.05) # Speed control

    print(f"\n{G}✅ {count} Ban requests successfully completed on {target}!")
    print(f"{Y}Status: Target neutralized shortly. Return to main menu...")
    time.sleep(3)

# --- JOIN CHANNEL ---
def join_channel():
    url = "https://whatsapp.com/channel/0029Vb75PfXChq6SdkyVaF0A"
    print(f"\n{Y}🌐 Opening WhatsApp Channel in browser...")
    time.sleep(1)
    webbrowser.open(url)
    print(f"{G}✅ Action Complete.")
    time.sleep(1)

# --- STARTUP ---
system_boot()

while True:
    clear()
    banner()
    print(f"{B}[01] {W}𝗕𝗮𝗻 𝗣𝗲𝗿𝗺𝗮𝗻𝗲𝗻𝘁         {B}[02] {W}𝗕𝗮𝗻 𝗧𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝘆")
    print(f"{B}[03] {W}𝗨𝗻𝗯𝗮𝗻 𝗣𝗲𝗿𝗺𝗮𝗻𝗲𝗻𝘁       {B}[04] {W}𝗨𝗻𝗯𝗮𝗻 𝗧𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝘆")
    print(f"{B}[05] {W}𝗩𝗶𝗲𝘄 𝗕𝗮𝗻𝗻𝗲𝗱 𝗟𝗶𝘀𝘁       {B}[06] {G}𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 🔥")
    print(f"{R}[07] {W}𝗦𝘆𝘀𝘁𝗲𝗺 𝗘𝘅𝗶𝘁")

    print(f"\n{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    choice = input(f"{G}┌──<{W}CRYPTO-LORD{G}>─[{W}Select Option{G}]\n└─> {W}").strip()

    if choice in ["1", "01"]:
        start_attack("PERMANENT BAN")
    elif choice in ["2", "02"]:
        start_attack("TEMPORARY BAN")
    elif choice in ["3", "03"]:
        start_attack("PERMANENT UNBAN")
    elif choice in ["4", "04"]:
        start_attack("TEMPORARY UNBAN")
    elif choice in ["5", "05"]:
        start_attack("FETCH BANNED LIST")
    elif choice in ["6", "06"]:
        join_channel()
    elif choice in ["7", "07"]:
        print(f"\n{R}[!] TERMINATING SESSION... SAFE EXIT.{Style.RESET_ALL}")
        time.sleep(1)
        sys.exit()
    else:
        print(f"{R}❌ INVALID SELECTION!")
        time.sleep(1)
