import time
import sys

# ASCII Art Banner
def print_banner():
    banner = """
    
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   ███████╗███████╗ ██████╗ ██████╗███████╗████████╗██╗   ██╗ ║
║   ██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝╚══██╔══╝╚██╗ ██╔╝ ║
║   █████╗  ███████╗██║     ██║     █████╗     ██║    ╚████╔╝  ║
║   ██╔══╝  ╚════██║██║     ██║     ██╔══╝     ██║     ╚██╔╝   ║
║   ██║     ███████║╚██████╗╚██████╗███████╗   ██║      ██║    ║
║   ╚═╝     ╚══════╝ ╚═════╝ ╚═════╝╚══════╝   ╚═╝      ╚═╝    ║
║                                                               ║
║                "Hello Friend"                                ║
║          Welcome to Mr. Robot fsociety Tools v2.0            ║
║                                                               ║
║              We are not larp we are fscoeiry       ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def slow_print(text, delay=0.05):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_menu():
    menu = """
┌─────────────────────────────────────────────────────┐
│              AVAILABLE TOOLS                        │
├─────────────────────────────────────────────────────┤
│ [1] NetworkXploit - Network Reconnaissance Tool    │
│ [2] CipherVault - Encryption/Decryption Suite      │
│ [3] DataHarvester - Information Gathering Module   │
│ [4] SystemShadow - System Analysis & Monitoring    │
│ [5] ProxyChain - Anonymous Network Routing         │
│ [6] MemoryErase - Trace Elimination Protocol       │
│ [7] AccessKey - Multi-Protocol Access Tool         │
│ [8] PulseMonitor - Real-time Threat Detection      │
│ [9] About fsociety                                 │
│ [0] Exit                                            │
└─────────────────────────────────────────────────────┘
    """
    print(menu)

def tool_1():
    print("\n[*] Initializing NetworkXploit v3.2...")
    time.sleep(0.5)
    print("[+] Scanning network topology...")
    time.sleep(1)
    print("[+] Identifying vulnerable endpoints...")
    time.sleep(1)
    print("[+] Mapping network routes: 42 nodes detected")
    time.sleep(0.5)
    print("[!] Operation simulated - This is for LARP entertainment only\n")

def tool_2():
    print("\n[*] Loading CipherVault v4.1...")
    time.sleep(0.5)
    print("[+] AES-256 Engine Ready")
    time.sleep(0.5)
    print("[+] RSA Key Generation: 2048-bit")
    time.sleep(0.5)
    print("[+] Hash Function: SHA-512")
    time.sleep(0.5)
    print("[!] Encryption simulation complete - For roleplay use only\n")

def tool_3():
    print("\n[*] Activating DataHarvester Module...")
    time.sleep(0.5)
    print("[+] Web crawler initialized...")
    time.sleep(1)
    print("[+] Analyzing metadata patterns...")
    time.sleep(1)
    print("[+] Data correlation engine active...")
    time.sleep(0.5)
    print("[~] Collecting: 127,432 data points")
    time.sleep(0.5)
    print("[!] This is simulated data for entertainment purposes\n")

def tool_4():
    print("\n[*] Deploying SystemShadow v2.8...")
    time.sleep(0.5)
    print("[+] Process monitoring enabled")
    time.sleep(0.5)
    print("[+] Memory analysis: 4,832 MB")
    time.sleep(0.5)
    print("[+] CPU Usage: 23%")
    time.sleep(0.5)
    print("[+] System processes tracked: 847")
    time.sleep(0.5)
    print("[!] Simulated monitoring only - LARP roleplay\n")

def tool_5():
    print("\n[*] Routing through ProxyChain v5.0...")
    time.sleep(0.5)
    print("[+] Establishing proxies...")
    time.sleep(0.5)
    print("[+] Proxy Chain: 23 nodes")
    time.sleep(0.5)
    print("[+] IP Spoofing: ACTIVE")
    time.sleep(0.5)
    print("[+] Traffic encryption: 256-bit")
    time.sleep(0.5)
    print("[!] Anonymous routing simulated - Roleplay only\n")

def tool_6():
    print("\n[*] Initiating MemoryErase Protocol...")
    time.sleep(0.5)
    print("[+] Secure deletion: ENABLED")
    time.sleep(0.5)
    print("[+] Log files: PURGED")
    time.sleep(0.5)
    print("[+] Cache memory: CLEARED")
    time.sleep(0.5)
    print("[+] Trace mitigation: 99.8%")
    time.sleep(0.5)
    print("[!] For fictional LARP scenarios only\n")

def tool_7():
    print("\n[*] Activating AccessKey v3.9...")
    time.sleep(0.5)
    print("[+] SSH - SSH v2 Protocol")
    time.sleep(0.3)
    print("[+] FTP - File Transfer Protocol")
    time.sleep(0.3)
    print("[+] HTTP/HTTPS - Web Protocol")
    time.sleep(0.3)
    print("[+] TELNET - Remote Access")
    time.sleep(0.3)
    print("[+] VNC - Virtual Network Computing")
    time.sleep(0.5)
    print("[!] Simulated access protocols - Entertainment use\n")

def tool_8():
    print("\n[*] Starting PulseMonitor v2.4...")
    time.sleep(0.5)
    print("[+] Threat Intelligence Feed: ACTIVE")
    time.sleep(0.5)
    print("[+] Anomaly Detection: RUNNING")
    time.sleep(0.5)
    print("[+] IDS/IPS Signature Database: Updated")
    time.sleep(0.5)
    print("[+] Current Threat Level: ████████░░ 78%")
    time.sleep(0.5)
    print("[!] Fictional threat detection for LARP purposes\n")

def about_fsociety():
    about = """
╔═══════════════════════════════════════════════════════════════╗
║                   ABOUT FSOCIETY                              ║
├═══════════════════════════════════════════════════════════════┤
║                                                               ║
║  "We are fsociety. We are the ones who control the network.  ║
║   We are the invisible hand. The ones pulling all the        ║
║   strings."                                                  ║
║                                                               ║
║  fsociety is a fictional hacker collective from the show     ║
║  Mr. Robot. This tool suite is designed for LARP, cosplay,   ║
║  and entertainment purposes only.                            ║
║                                                               ║
║  All functions are simulated and for roleplay scenarios.     ║
║  This is NOT intended for any illegal or harmful activities. ║
║                                                               ║
║  Stay true to the Revolution... in your imagination.         ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """
    print(about)

def main():
    print_banner()
    slow_print("[*] System initializing...", delay=0.03)
    time.sleep(1)
    
    while True:
        print_menu()
        choice = input("[elliot@fsociety ~]$ ").strip()
        
        if choice == "1":
            tool_1()
        elif choice == "2":
            tool_2()
        elif choice == "3":
            tool_3()
        elif choice == "4":
            tool_4()
        elif choice == "5":
            tool_5()
        elif choice == "6":
            tool_6()
        elif choice == "7":
            tool_7()
        elif choice == "8":
            tool_8()
        elif choice == "9":
            about_fsociety()
        elif choice == "0":
            print("\n[*] Disconnecting from fsociety network...")
            time.sleep(0.5)
            slow_print("[+] Goodbye, Friend.", delay=0.08)
            time.sleep(1)
            break
        else:
            print("[!] Invalid option. Please try again.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Connection terminated by user.")
        print("[*] See you around, Friend...\n")
