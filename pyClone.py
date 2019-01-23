#!/usr/bin/env python3
import os
import sys
"""
Author  - pyCity
Date    - 22th January 2019
Version - 1.0

Usage:         python pyClone.py

Description:   Quick downloader for some common red-team repos
"""

# Dictionary for download links Feel free to add your own. Don't forget any extras to add to menu.
Links = {
        "nmap"        : "https://github.com/nmap/nmap",
        "dbd"         : "https://github.com/gitdurandal/dbd",
        "cryptit"     : "https://github.com/Dforwood/cryptit",
        "metasploit"  : "https://github.com/rapid7/metasploit-framework",
        "diamorphine" : "https://github.com/m0nad/Diamorphine",
        "vegile"      : "https://github.com/Screetsec/Vegile",
        "vlany"       : "https://github.com/mempodippy/vlany",
        "keylogger"   : "https://github.com/GiacomoLaw/Keylogger",
        "shellver"    : "https://github.com/0xR0/shellver",
        "ares"        : "https://github.com/sweetsoftware/Ares",
        "byob"        : "https://github.com/malwaredllc/byob"
        }


def menu():
    print("Welcome to pyDownloader. Your options are:\n")
    print("nmap        - Vulnerability Scanner/Backdoor\n"
          "dbd         - Encrypted Backdoor Daemon\n"
          "cryptit     - AES Encryption/Decryption tool\n"
          "metasploit  - Exploitation Framework\n"
          "diamorphine - LKM kernal Rootkit 2.6.x/3.x/4.x (x86 and x86_64)\n"
          "vegile      - Rootkit/Process hider\n"
          "vlany       - LD_PRELOAD Rootkit (x86 and x86_64)\n"
          "keylogger   - Multi-platform keylogger with persistence\n"
          "shellver    - Reverse shell cheat sheet (similar to msfvenom)\n"
          "ares        - Botnet/C2 Server with backdoor\n"
          "byob        - Botnet/C2 Server\n"
          "all         - Download all repositories\n"
          "exit        - sys.exit()\n")


        
def checkGit():
    """Verify that git is installed, otherwise exit"""

    git_exists = os.path.exists("/usr/bin/git") # Assign variable to boolean
    if git_exists:
        print("Git found! Continuing....")
    else:
        print("Git not detected. Trying once more...")
        last_check = os.system("command -v git")
        if last_check:
            print(last_check)
        else:
            sys.exit()

        

def cloneRepo():
    """Downloads tools via os.system"""

    while True:
        tool = input("Enter a tool to download: ")
        if tool in Links:
            print("Cloning {}......".format(tool))
            os.system("git clone " + Links[tool])
        if tool == "exit":
            print("Exiting....")
            sys.exit()
        if tool == "":
            continue
        if tool == "all":
            warning = input("Are you sure you would like to download everything? (y/n)")
            if warning == "y":
                clone_all()
            if warning == "n":
                continue
            else:
                print("Please enter a valid option")
        else:
            print("Please enter a valid option (e.g., nmap)")

        

def clone_all():
    """Download everything in Links Array"""
    print("Cloning all repos...")
    for i in Links.values():
        print("Cloning {}".format(i))
        os.system("git clone {}".format(i))



if __name__ == "__main__":
    os.system("clear")
    checkGit()
    menu()
    cloneRepo()
