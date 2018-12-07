#!/usr/bin/env python3
import os, os.path
import sys

"""Quick downloader script for my commonly used github repos"""

# Dictionary for download links Feel free to add your own. Don't forget any extras to add to menu.
Links = {
        "nmap"        : "https://github.com/nmap/nmap",
        "dbd"         : "https://github.com/gitdurandal/dbd",
        "cryptit"     : "https://github.com/Dforwood/cryptit",
        "metasploit"  : "https://github.com/rapid7/metasploit-framework",
        "diamorphine" : "https://github.com/m0nad/Diamorphine",
        "vegile"      : "https://github.com/Screetsec/Vegile",
        "vlany"       : "https://github.com/mempodippy/vlany",
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
          "ares        - Botnet/C2 Server with backdoor\n"
          "byob        - Botnet/C2 Server\n"
          "all         - Download all repositories\n"
          "exit        - sys.exit()\n")


def check_for_git():
    """Verify that git is installed, otherwise exit"""
    git_exists = os.path.exists("/usr/bin/git") # Assign variable to boolean
    if git_exists:
        print("Git found! Continuing....")
    else:
        print("Git not detected. Please install Git before using this script.")
        sys.exit()


def clone_repo():
    """Downloads tools via git clone"""
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


def install_file():
    #TODO add installer for any that requrie it. e.g., nmap - ./configure && make && make install"""
    pass


def main():
    os.system("clear")
    check_for_git()
    menu()
    clone_repo()


if __name__ == "__main__":
    main()
