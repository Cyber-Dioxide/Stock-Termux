from scripts.sprint import command , sprint
from scripts.banner import banner , clear,banner2
from scripts.colors import r,y,c,g,ran
from time import sleep
clear()

banner()

def main():
    sprint(r + "Scanning junk files of termux...")
    sleep(2)
    sprint(c + "Making things ready...")
    sleep(1)
    sprint(y + "Installing packages...")
    command("apt install fish")
    command("apt install zsh")
    sleep(1)
    sprint(g + "Preparing...")
    command("cd $PREFIX/etc")
    command("rm - rf motd")
    command("rm -rf motd-playstore")
    command("rm -rf motd.dpkg-dist")
    clear()
    banner2()

    command("chsh -s fish")
    command("curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish")
    command("omf install agnoster")

    clear()

    sprint(ran+"\n\n Restart your termux to see changes")
    command("exit")

if __name__ == '__main__':
    main()