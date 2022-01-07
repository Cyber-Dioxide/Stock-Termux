from scripts.sprint import command , sprint
from scripts.banner import banner , clear,banner2
from scripts.colors import r,y,c,g,ran
from time import sleep
clear()
def make(filename,name):
	file = open(filename,"a+")
	file.write(name)
	file.close()
	return True


banner()
def main():
	sprint(r + "Scanning junk files of termux...")
	sleep(2)
	sprint(c + "Making things ready...")
	sleep(1)
	sprint(y + "Installing packages...")
	clear()
	banner2()
	a = input(f"{r}[1] {y}Zsh Theme\n{r}[2] {y}Fish Theme\n{ran}~Stock@temrux~> ")
	if a == "1":
			command('apt install zsh -y && sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
			command("chsh -s $(which zsh)")
			make("~/.zshrc",'ZSH_THEME="agnoster" ')

	elif a == "2":
			command('apt install fish -y && curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish && omf install agnoster')
			command("chsh -s $(which fish)")
			make("~/.config/fish/config.fish",'set fish_greeting')

	else:
			exit("Unexpected Error")

	sprint(g + "Preparing...")

	command("rm -rf $PREFIX/motd*")

	clear()
	banner2()

   

	clear()

	sprint(ran+"\n\n Restart your termux to see changes")
	command("exit")

if __name__ == '__main__':
	main()
