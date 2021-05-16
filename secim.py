import os , sys , time
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
print("")
print("""

    1) Wep Cracking
    2) Wpa2 Cracking
    3) Deauth Attack

""")

soru = input("root@eyll:~# ")
if soru == '1':
    os.system("python3 main.py")
    exit()
elif soru == '2':
    os.system("python3 wpa2.py")
elif soru == '3':
    os.system("python3 attack.py")