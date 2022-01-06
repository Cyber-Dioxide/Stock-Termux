from scripts.sprint import command , sprint
import os
from scripts.banner import banner , clear
from scripts.colors import r,y,c,g,ran
from time import sleep
clear()

banner()

def main():
    sprint(r + "Scanning junk files of termux...")
    sleep(2)
    sprint(y + "Installing packages...")
    command("apt install fish")
    command("apt install zsh")
    sleep(1)
    sprint(g + "Preparing...")
    command("cd $PREFIX/etc")
    command("rm - rf motd")
    try:
        os.remove("motd")
    except Exception:
        pass

    clear()
    command("chsh -s fish")
    sprint(ran+"\n\n Restart your termux")
    sprint(c+"\nExitting Temux...")

    command("exit")




if __name__ == '__main__':
    main()