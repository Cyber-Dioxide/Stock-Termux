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

    print(r+"\n[1] "+c +"Install fish theme\n")
    print(r +"[2] "+c +"Install zsh theme")
    choice = input(ran + '\n~Stock@Trmux~> ')

    if choice == "1":
        command("chsh -s fish")

    else:
        command("chsh -s zsh")

    clear()

    sprint(ran+"\n\n Restart your termux to see changes")
    command("exit")

if __name__ == '__main__':
    main()