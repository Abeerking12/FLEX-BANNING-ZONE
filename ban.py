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

# --- CONFIGURATION ---
SENDER_EMAIL = os.getenv('GMAIL_ADDRESS')
SENDER_PASSWORD = os.getenv('GMAIL_PASSWORD')
SUPPORT_EMAILS = ["support@whatsapp.com", "abuse@support.whatsapp.com"]

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# --- HEAVY BOOT ANIMATION ---
def system_boot():
    clear()
    print(f"{C}[SYSTEM INFO] Initializing Crypto Lord Kernel v3.0...")
    time.sleep(1)
    for i in range(1, 5):
        print(f"{W}[{G}LOG{W}] Protocol-0{i} Connected... Status: {G}SECURE")
        time.sleep(0.3)
    
    print(f"\n{Y}[!] DECRYPTING BANNING DATABASE...")
    for i in range(0, 101, 20):
        sys.stdout.write(f"\r{W}[{M}{'#' * (i//5)}{' ' * (20 - i//5)}{W}] {i}% Complete")
        sys.stdout.flush()
        time.sleep(0.2)
    print(f"\n\n{G}✔️ SYSTEM BYPASS SUCCESSFUL\n{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    time.sleep(1)

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

# --- ACTUAL ATTACK LOGIC WITH RED ANIMATION ---
def start_attack(mode_name):
    clear()
    banner()
    print(f"{M}[ SYSTEM MODE: {mode_name} ]")
    
    # 1. Target Number Poochna
    target = input(f"\n{R}[#] {G}ENTER TARGET (With Country Code): {W}").strip()
    if not target:
        print(f"{R}❌ Error: Target Required!")
        time.sleep(2)
        return

    # 2. Report Count Poochna
    try:
        count = int(input(f"{R}[#] {G}HOW MANY REPORTS TO SEND?: {W}"))
    except:
        print(f"{R}❌ Error: Invalid Count!")
        time.sleep(2)
        return

    print(f"\n{Y}[!] INITIALIZING HEAVY PACKETS FOR {target}...")
    time.sleep(1.5)

    # 3. RED FAKE ANIMATION (Jaisa pic mein tha)
    for i in range(1, count + 1):
        # Professional Red Logs
        print(f"{R}Sending Attack to {target} Amount {i}")
        time.sleep(0.05) # Fast speed for heavy look

    # Final Success Message
    print(f"\n{G}✅ {count} Ban was successfully completed🔥💯 on Target🎯 {target}.")
    print(f"{R}Number {target} Will be permanently Banned Shortly Stay tuned.")
    
    # Optional: Email try karna (Background mein)
    # yahan aap send_report(target, mode_name, count) call kar sakte hain.

    input(f"\n{W}Press Enter to Return to Main Frame...")

# --- MAIN LOOP ---
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
        start_attack("LIST CHECK")
    elif choice in ["6", "06"]:
        webbrowser.open("https://whatsapp.com/channel/0029Vb75PfXChq6SdkyVaF0A")
    elif choice in ["7", "07"]:
