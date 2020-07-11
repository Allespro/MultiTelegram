import os
import subprocess
import menupy

DataDir = '/home/alles/.MyTelegram' # Where accounts will be located
Binary = '/usr/bin/telegram-desktop' # Where is Telegram binary

def CheckPatches():
	if os.path.exists(DataDir) == False:
		try:
			os.mkdir(DataDir)
		except OSError:
			exit("Can't create %s" % path)
		else:
			print ("Directory %s created!" % path)
	if os.path.exists(Binary) == False:
		exit("No Telegram binary!")


def MainMenu(msg):
	SelectMenu = menupy.OptionMenu(str(msg), title_color="cyan")
	SelectMenu.add_option("Login to an existing account", color="green", ret="exist")
	SelectMenu.add_option("Login to a new account", color="green", ret="new")
	SelectMenu.add_option("Exit", color="red", ret="exit")
	result = SelectMenu.run()
	if result == "exit":
		exit("Have a nice day!")
	else:
		return result


def SelectAccount():
	AccountsDirs = os.listdir(DataDir)
	SelectMenu = menupy.OptionMenu("Select Telegram account:", title_color="cyan")
	for Dir in AccountsDirs:
		SelectMenu.add_option(Dir, color="green", ret=str(Dir))
	SelectMenu.add_option("To main menu", color="red", ret="main")
	result = SelectMenu.run()
	if result == "main":
		main("By @Allespro, Thanks to @luxunator for this wonderful menu\nSelect option:")
	else:
		return result

def NewAccount():
	AccountName = str(input("Input your account name: "))
	if os.path.exists(DataDir+"/"+AccountName):
		main("Account %s is already created!" % AccountName)
	else:
		try:
			os.mkdir(DataDir+"/"+AccountName)
		except OSError:
			main("Can't create %s" % AccountName)
		else:
			main("Directory for account %s created! Now you can login!" % AccountName)

def main(mainmsg):
	chs = MainMenu(str(mainmsg)) 
	if chs == "exist":
		Account = SelectAccount()
		command = str(Binary) + " -many -workdir " + DataDir+ "/" + Account
		subprocess.Popen(command, shell=True)
		exit("\n\nFollow me on Github\nhttps://github.com/Allespro\n\n")
	elif chs == "new":
		NewAccount()
	else:
		exit('HOW YOU GET THAT RETURN???')

if __name__ == '__main__':
	CheckPatches()
	main("By @Allespro, Thanks to @luxunator for this wonderful menu\nSelect option:")
