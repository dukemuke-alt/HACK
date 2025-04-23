import time
import sys
import os
from colorama import init, Fore, Style

# Initialize colorama
init()

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_slow(text, color=Fore.WHITE, delay=0.03):
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_animation(duration, message):
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    start_time = time.time()
    while time.time() - start_time < duration:
        for char in chars:
            sys.stdout.write(f"\r{Fore.RED}[{char}] {message}{' ' * 20}")
            sys.stdout.flush()
            time.sleep(0.1)
    print()

def validate_youtube_url(url):
    return "youtube.com" in url.lower() or "youtu.be" in url.lower()

def main():
    clear_screen()
    # YouTube-style header
    print_slow(f"{Fore.RED}██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗{Style.RESET_ALL}", Fore.RED)
    print_slow(f"{Fore.RED}╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝{Style.RESET_ALL}", Fore.RED)
    print_slow(f"{Fore.RED} ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝█████╗  {Style.RESET_ALL}", Fore.RED)
    print_slow(f"{Fore.RED}  ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝  {Style.RESET_ALL}", Fore.RED)
    print_slow(f"{Fore.RED}   ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██║  ██║███████╗{Style.RESET_ALL}", Fore.RED)
    print_slow(f"{Fore.RED}   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝{Style.RESET_ALL}", Fore.RED)
    print_slow(f"{Fore.RED}YouTube Account Hacker v4.0.2{Style.RESET_ALL}", Fore.RED)
    print_slow(f"{Fore.RED}{'=' * 50}{Style.RESET_ALL}")
     # Credits
    print_slow(f"\n{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}Made by: Rajdeep Chaudhury{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}Instagram: @black_rajdeep{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
    print_slow(f"{Fore.RED}Initializing YouTube hacking protocol...{Style.RESET_ALL}")
    time.sleep(2)
    
    print_slow(f"{Fore.CYAN}[*] System Information:{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}[+] IP Address: 192.168.1.1{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}[+] MAC Address: 00:1A:2B:3C:4D:5E{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}[+] Port: 443{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}[+] Protocol: TCP{Style.RESET_ALL}")
    time.sleep(1)
    
    print_slow(f"{Fore.YELLOW}[*] Scanning for vulnerabilities...{Style.RESET_ALL}")
    time.sleep(2)
    
    # Vulnerability scanning
    vulns = [
        "YouTube Data API Exploit",
        "OAuth Token Hijacking",
        "Session Fixation",
        "Clickjacking Vulnerability",
        "XSS Injection",
        "SQL Injection",
        "CSRF Token Vulnerability",
        "Broken Authentication",
        "Security Misconfiguration",
        "API Key Leak",
        "Video ID Enumeration",
        "Channel ID Exploit",
        "Playlist Access Vulnerability",
        "Comment System Exploit",
        "Subscriber Count Manipulation"
    ]
    for vuln in vulns:
        print_slow(f"{Fore.YELLOW}[*] Checking for {vuln}...{Style.RESET_ALL}")
        time.sleep(0.3)
        print_slow(f"{Fore.GREEN}[+] {vuln} vulnerability found!{Style.RESET_ALL}")
    
    while True:
        target = input(f"{Fore.RED}[+] Enter YouTube channel/video link: {Style.RESET_ALL}")
        if validate_youtube_url(target):
            break
        print_slow(f"{Fore.RED}[-] Invalid YouTube URL. Please enter a valid YouTube link.{Style.RESET_ALL}")
    
    print_slow(f"\n{Fore.CYAN}[+] Target acquired: {target}{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}[+] Starting port scan...{Style.RESET_ALL}")
    
    # Port scanning animation
    for i in range(1, 11):
        print_slow(f"{Fore.YELLOW}[*] Scanning port {i*1000}...{Style.RESET_ALL}")
        time.sleep(0.5)
    
    print_slow(f"{Fore.GREEN}[+] Port 443 is open{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}[+] Establishing connection...{Style.RESET_ALL}")
    time.sleep(2)
    
    # Main hacking sequence
    print_slow(f"{Fore.YELLOW}[*] Starting attack sequence...{Style.RESET_ALL}")
    time.sleep(1)
    
    loading_animation(5, "Bypassing YouTube security")
    loading_animation(5, "Exploiting YouTube Data API")
    loading_animation(5, "Cracking password encryption")
    loading_animation(5, "Accessing user database")
    loading_animation(5, "Decrypting password")
    loading_animation(5, "Bypassing 2FA")
    loading_animation(5, "Extracting access tokens")
    loading_animation(5, "Bypassing rate limits")
    loading_animation(5, "Establishing persistent connection")
    loading_animation(5, "Covering tracks")
    
    # Display "hacked" information
    print_slow(f"\n{Fore.GREEN}[+] Success! Account credentials found:{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Gmail: {target.split('/')[-1]}@gmail.com{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Password: YouTube@123{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Last Login: 2024-03-15 14:30:45{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Account Created: 2010-01-01{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] 2FA: Disabled{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Recovery Email: recovery@{target.split('/')[-1]}.com{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Recovery Phone: +1 234-567-8901{Style.RESET_ALL}")
    
    print_slow(f"\n{Fore.YELLOW}[!] Press Enter to exit...{Style.RESET_ALL}")
    input()
    
    # Credits
    print_slow(f"\n{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}Made by: Rajdeep Chaudhury{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}Instagram: @black_rajdeep{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")

if __name__ == "__main__":
    main() 