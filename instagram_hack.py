import time
import random
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

def generate_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

def generate_mac():
    return ":".join([f"{random.randint(0, 255):02x}" for _ in range(6)])

def loading_animation(duration, message):
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    start_time = time.time()
    while time.time() - start_time < duration:
        for char in chars:
            sys.stdout.write(f"\r{Fore.MAGENTA}[{char}] {message}{' ' * 20}")
            sys.stdout.flush()
            time.sleep(0.1)
    print()

def generate_random_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

def main():
    clear_screen()
    # Instagram-style header with gradient effect
    print_slow(f"{Fore.MAGENTA}██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ███████╗██████╗ {Style.RESET_ALL}", Fore.MAGENTA)
    print_slow(f"{Fore.MAGENTA}██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔════╝██╔══██╗{Style.RESET_ALL}", Fore.MAGENTA)
    print_slow(f"{Fore.MAGENTA}██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗█████╗  ██████╔╝{Style.RESET_ALL}", Fore.MAGENTA)
    print_slow(f"{Fore.MAGENTA}██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══╝  ██╔══██╗{Style.RESET_ALL}", Fore.MAGENTA)
    print_slow(f"{Fore.MAGENTA}██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝███████╗██║  ██║{Style.RESET_ALL}", Fore.MAGENTA)
    print_slow(f"{Fore.MAGENTA}╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝{Style.RESET_ALL}", Fore.MAGENTA)
    print_slow(f"{Fore.MAGENTA}Instagram Account Hacker v3.0.1{Style.RESET_ALL}", Fore.MAGENTA)
    print_slow(f"{Fore.MAGENTA}{'=' * 50}{Style.RESET_ALL}")
    
    # Credits
    print_slow(f"\n{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}Made by: Rajdeep Chaudhury{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}Instagram: @black_rajdeep{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
    
    print_slow(f"{Fore.MAGENTA}Initializing Instagram hacking protocol...{Style.RESET_ALL}")
    time.sleep(2)
    
    # Generate random system info
    ip = generate_ip()
    mac = generate_mac()
    port = random.randint(1000, 9999)
    
    print_slow(f"{Fore.CYAN}[*] System Information:{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}[+] IP Address: {ip}{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}[+] MAC Address: {mac}{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}[+] Port: {port}{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}[+] Protocol: TCP{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}[+] OS: Linux 6.11.0-21-generic{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}[+] Browser: Chrome 122.0.6261.112{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}[+] User Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36{Style.RESET_ALL}")
    time.sleep(1)
    
    print_slow(f"{Fore.YELLOW}[*] Scanning for vulnerabilities...{Style.RESET_ALL}")
    time.sleep(2)
    
    # Vulnerability scanning with more technical details
    vulns = [
        "SQL Injection in Instagram API",
        "XSS in Direct Messages",
        "CSRF Token Bypass",
        "Session Hijacking",
        "OAuth Token Theft",
        "API Rate Limit Bypass",
        "GraphQL Query Injection",
        "Media Upload Exploit",
        "Account Takeover via Password Reset",
        "Instagram API Key Leak",
        "Story View Exploit",
        "Location Data Leak",
        "Two-Factor Authentication Bypass",
        "Instagram WebSocket Hijacking",
        "Instagram CDN Exploit"
    ]
    
    for vuln in vulns:
        print_slow(f"{Fore.YELLOW}[*] Checking for {vuln}...{Style.RESET_ALL}")
        time.sleep(0.3)
        if random.random() > 0.7:
            print_slow(f"{Fore.GREEN}[+] {vuln} vulnerability found!{Style.RESET_ALL}")
            print_slow(f"{Fore.GREEN}[+] Severity: {random.choice(['Critical', 'High', 'Medium'])}{Style.RESET_ALL}")
            print_slow(f"{Fore.GREEN}[+] CVE: CVE-2024-{random.randint(1000, 9999)}{Style.RESET_ALL}")
        else:
            print_slow(f"{Fore.RED}[-] {vuln} not vulnerable{Style.RESET_ALL}")
    
    target = input(f"{Fore.MAGENTA}[+] Enter Instagram username or profile link: {Style.RESET_ALL}")
    
    print_slow(f"\n{Fore.CYAN}[+] Target acquired: {target}{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}[+] Starting port scan...{Style.RESET_ALL}")
    
    # Port scanning animation with more technical details
    for i in range(1, 11):
        port = i * 1000
        print_slow(f"{Fore.YELLOW}[*] Scanning port {port}...{Style.RESET_ALL}")
        if port in [80, 443, 8080]:
            print_slow(f"{Fore.GREEN}[+] Port {port} is open (HTTP/HTTPS){Style.RESET_ALL}")
        time.sleep(0.5)
    
    print_slow(f"{Fore.GREEN}[+] Port {port} is open{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}[+] Establishing connection...{Style.RESET_ALL}")
    time.sleep(2)
    
    # Main hacking sequence with more technical details
    print_slow(f"{Fore.YELLOW}[*] Starting attack sequence...{Style.RESET_ALL}")
    time.sleep(1)
    
    loading_animation(5, "Bypassing Instagram security")
    loading_animation(5, "Injecting GraphQL payload")
    loading_animation(5, "Cracking password encryption")
    loading_animation(5, "Accessing Instagram API")
    loading_animation(5, "Decrypting session tokens")
    loading_animation(5, "Bypassing 2FA")
    loading_animation(5, "Extracting OAuth tokens")
    loading_animation(5, "Bypassing rate limits")
    loading_animation(5, "Establishing WebSocket connection")
    loading_animation(5, "Covering tracks")
    
    # Generate random session info with more technical details
    session_id = ''.join(random.choices('0123456789ABCDEF', k=32))
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    access_token = ''.join(random.choices('0123456789ABCDEF', k=64))
    device_id = ''.join(random.choices('0123456789', k=15))
    android_id = ''.join(random.choices('0123456789abcdef', k=16))
    uuid = ''.join(random.choices('0123456789abcdef', k=32))
    
    print_slow(f"\n{Fore.GREEN}[+] Success! Account credentials found:{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Username: {target}{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Password: {generate_random_password()}{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Session ID: {session_id}{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Access Token: {access_token}{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Device ID: {device_id}{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Android ID: {android_id}{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] UUID: {uuid}{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Timestamp: {timestamp}{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Last Login: {time.strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Account Created: 2010-01-01{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] 2FA: Disabled{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Recovery Email: recovery@{target}.com{Style.RESET_ALL}")
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