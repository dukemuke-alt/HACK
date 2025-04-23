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
            sys.stdout.write(f"\r{Fore.BLUE}[{char}] {message}{' ' * 20}")
            sys.stdout.flush()
            time.sleep(0.1)
    print()

def generate_random_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "protonmail.com"]
    name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 10)))
    domain = random.choice(domains)
    return f"{name}@{domain}"

def generate_random_phone():
    return f"+1{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"

def validate_facebook_url(url):
    return "facebook.com" in url.lower() or "fb.com" in url.lower()

def main():
    clear_screen()
    # Facebook-style header
    print_slow(f"{Fore.BLUE}███████╗ █████╗  ██████╗███████╗██████╗  ██████╗  ██████╗ ██╗  ██╗{Style.RESET_ALL}", Fore.BLUE)
    print_slow(f"{Fore.BLUE}██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝{Style.RESET_ALL}", Fore.BLUE)
    print_slow(f"{Fore.BLUE}█████╗  ███████║██║     █████╗  ██████╔╝██║   ██║██║   ██║█████╔╝ {Style.RESET_ALL}", Fore.BLUE)
    print_slow(f"{Fore.BLUE}██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗██║   ██║██║   ██║██╔═██╗ {Style.RESET_ALL}", Fore.BLUE)
    print_slow(f"{Fore.BLUE}██║     ██║  ██║╚██████╗███████╗██████╔╝╚██████╔╝╚██████╔╝██║  ██╗{Style.RESET_ALL}", Fore.BLUE)
    print_slow(f"{Fore.BLUE}╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝{Style.RESET_ALL}", Fore.BLUE)
    print_slow(f"{Fore.BLUE}Facebook Account Hacker v3.2.1{Style.RESET_ALL}", Fore.BLUE)
    print_slow(f"{Fore.BLUE}{'=' * 50}{Style.RESET_ALL}")
    print_slow(f"{Fore.BLUE}Initializing Facebook hacking protocol...{Style.RESET_ALL}")
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
    time.sleep(1)
    
    print_slow(f"{Fore.YELLOW}[*] Scanning for vulnerabilities...{Style.RESET_ALL}")
    time.sleep(2)
    
    # Vulnerability scanning
    vulns = [
        "Graph API Exploit",
        "Access Token Leak",
        "CSRF Token Vulnerability",
        "Broken Authentication",
        "Security Misconfiguration",
        "OAuth Token Hijacking",
        "Session Fixation",
        "Clickjacking Vulnerability",
        "XSS Injection",
        "SQL Injection"
    ]
    for vuln in vulns:
        print_slow(f"{Fore.YELLOW}[*] Checking for {vuln}...{Style.RESET_ALL}")
        time.sleep(0.5)
        if random.random() > 0.7:
            print_slow(f"{Fore.GREEN}[+] {vuln} vulnerability found!{Style.RESET_ALL}")
        else:
            print_slow(f"{Fore.RED}[-] {vuln} not vulnerable{Style.RESET_ALL}")
    
    while True:
        target = input(f"{Fore.BLUE}[+] Enter Facebook profile link: {Style.RESET_ALL}")
        if validate_facebook_url(target):
            break
        print_slow(f"{Fore.RED}[-] Invalid Facebook URL. Please enter a valid Facebook profile link.{Style.RESET_ALL}")
    
    print_slow(f"\n{Fore.CYAN}[+] Target acquired: {target}{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}[+] Starting port scan...{Style.RESET_ALL}")
    
    # Port scanning animation
    for i in range(1, 11):
        print_slow(f"{Fore.YELLOW}[*] Scanning port {i*1000}...{Style.RESET_ALL}")
        time.sleep(0.5)
    
    print_slow(f"{Fore.GREEN}[+] Port {port} is open{Style.RESET_ALL}")
    print_slow(f"{Fore.CYAN}[+] Establishing connection...{Style.RESET_ALL}")
    time.sleep(2)
    
    # Main hacking sequence
    print_slow(f"{Fore.YELLOW}[*] Starting attack sequence...{Style.RESET_ALL}")
    time.sleep(1)
    
    loading_animation(5, "Bypassing Facebook security")
    loading_animation(5, "Exploiting Graph API")
    loading_animation(5, "Cracking password encryption")
    loading_animation(5, "Accessing user database")
    loading_animation(5, "Decrypting password")
    loading_animation(5, "Bypassing 2FA")
    loading_animation(5, "Extracting access tokens")
    loading_animation(5, "Bypassing rate limits")
    loading_animation(5, "Establishing persistent connection")
    loading_animation(5, "Covering tracks")
    
    # Generate random session info
    session_id = ''.join(random.choices('0123456789ABCDEF', k=32))
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    access_token = ''.join(random.choices('0123456789ABCDEF', k=64))
    user_id = ''.join(random.choices('0123456789', k=15))
    email = generate_random_email()
    phone = generate_random_phone()
    
    print_slow(f"\n{Fore.GREEN}[+] Success! Account credentials found:{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Email: {email}{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Phone: {phone}{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Password: {generate_random_password()}{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Session ID: {session_id}{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Access Token: {access_token}{Style.RESET_ALL}")
    print_slow(f"{Fore.GREEN}[+] Timestamp: {timestamp}{Style.RESET_ALL}")
    
    print_slow(f"\n{Fore.YELLOW}[!] Press Enter to exit...{Style.RESET_ALL}")
    input()

if __name__ == "__main__":
    main() 