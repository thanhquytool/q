import os
import requests
import sys
from time import sleep
import json
import base64
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from datetime import datetime
from rich.console import Console
from rich.table import Table
KEY_FILE = "thanhquytoolkey.txt"
console = Console()
def decrypt_data(encrypted_data):
    return base64.b64decode(encrypted_data.encode()).decode()
def check_saved_key():
    if not os.path.exists(KEY_FILE):
        return False, "Không tìm thấy key đã lưu!"
    try:
        with open(KEY_FILE, "r") as file:
            encrypted_data = file.read()
            data = json.loads(decrypt_data(encrypted_data))
            key = data.get("key", "")
            expiration_date = datetime.fromisoformat(data["expiration_date"])
            if expiration_date > datetime.now():
                days_left = (expiration_date - datetime.now()).days
                return True, f"✅ Key hợp lệ! Hết hạn: {expiration_date.strftime('%Y-%m-%d %H:%M:%S')} ({days_left} ngày nữa)", key, days_left
            else:
                return False, "❌ Key đã hết hạn!", "", 0
    except:
        return False, "⚠️ Lỗi khi đọc file key!", "", 0
is_valid, message, key, days_left = check_saved_key()
hidden_key = key[:1] + "..." if key else "Không có key"
console.print(f"[bold yellow]{message}[/bold yellow]")
if not is_valid:
    console.print("\n[bold red]Yêu cầu nhập key mới![/bold red]")
    exit()
def banner():
 os.system("cls" if os.name == "nt" else "clear")
 banner = f"""
\033[1;32m████████╗ ██████╚╗         ████████╗ █████╗  █████╗ ██╗
\033[1;36m╚══██╔══╝██║   ██║         ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;32m   ██║   ██║   ██║   █████╗   ██║   ██║  ██║██║  ██║██║
\033[1;36m   ██║   ██║ ████╚╗  ╚════╝   ██║   ██║  ██║██║  ██║██║
\033[1;36m   ██║   ╚████████║           ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m   ╚═╝    ╚════╗\033[1;36m██\033[1;31m║           ╚═╝    ╚════╝  ╚════╝ ╚═════╝
\033[1;31m               ╚══╝
\033[1;37m══════════════════════════════════════════════════════════════
\033[1;37m[\033[1;91m📝\033[1;97m]\033[1;97m Admin    \033[1;31m: \033[1;32mThành Quý Tool
\033[1;97m[\033[1;91m📝\033[1;97m]\033[1;97m Telegram \033[1;31m: \033[1;36mhttps://t.me/quyleotop
\033[1;97m[\033[1;91m📝\033[1;97m]\033[1;97m Youtube  \033[1;31m: \033[1;31mhttps://www.youtube.com/@thanhquytool
\033[1;37m══════════════════════════════════════════════════════════════
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.0001)
  
def thongtinkey():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expiration_time = (datetime.now() + timedelta(days=days_left)).strftime("%Y-%m-%d %H:%M:%S") if days_left > 0 else "Hết hạn"
    console.print(f"[bold white]Key của bạn:[/bold white] {hidden_key}")
    console.print(f"[bold white]Thời hạn còn lại:[/bold white] {days_left} ngày")
    console.print("[bold white]══════════════════════════════════════════════════════════════[/bold white]")

def check_connection():
    try:
        response = requests.get("https://www.google.com.vn", timeout=3)        
    except (requests.exceptions.ReadTimeout, requests.ConnectionError):
        print("\033[1;31mVui lòng kiểm tra kết nối mạng !!!")
        sys.exit()
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"Lỗi: {str(e)}")    
while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	banner()
	thongtinkey()
	print (Colorate.Diagonal(Colors.blue_to_purple, "╔══════════════════════╗         "))
	print (Colorate.Diagonal(Colors.blue_to_purple, "║  Tool Auto Golike    ║          "))
	print (Colorate.Diagonal(Colors.blue_to_purple, "╚══════════════════════╝           "))
	print(f"\033[1;37m● \033[1;32m[🧸] \033[1;31m➩ \033[1;36mNhập Số \033[1;37m| \033[1;33m1.1 \033[1;37m| \033[1;35mTool Golike TikTok")
	print(f"\033[1;37m● \033[1;32m[🧸] \033[1;31m➩ \033[1;36mNhập Số \033[1;37m| \033[1;33m1.2 \033[1;37m| \033[1;35mTool Golike Twitter")
	print(f"\033[1;37m● \033[1;32m[🧸] \033[1;31m➩ \033[1;36mNhập Số \033[1;37m| \033[1;33m1.3 \033[1;37m| \033[1;35mTool Golike Instagram")
	print(f"\033[1;37m● \033[1;32m[🧸] \033[1;31m➩ \033[1;36mNhập Số \033[1;37m| \033[1;33m1.4 \033[1;37m| \033[1;35mTool Golike Linkedin")
	print("\033[1;37m══════════════════════════════════════════════════════════════")
	chon = input('\033[1;37m● \033[1;32m[🧸] \033[1;31m➩ \033[1;36mNhập Số: \033[1;33m')
	check_connection()
	print("\033[1;37m══════════════════════════════════════════════════════════════")
	print("\033[1;37m● \033[1;32mĐang Vào Tool - Vui Lòng Đợi...")        
	if chon == '1.1':
		exec(requests.get('https://raw.githubusercontent.com/thanhquytool/q/main/Golike/GolikeTikTok.py').text)
	elif chon == '1.2':
		exec(requests.get('https://raw.githubusercontent.com/thanhquybot/Menu/main/Golike/GolikeTwitter.py').text)
	elif chon == '1.3':
		exec(requests.get('https://raw.githubusercontent.com/thanhquybot/Menu/main/Golike/GolikeInstagram.py').text)
	elif chon == '1.4':
		exec(requests.get('https://raw.githubusercontent.com/thanhquybot/Menu/main/Golike/GolikeLinkedin.py').text)
	else:
		sys.exit("")