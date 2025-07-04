import os

from pyfzf.pyfzf import FzfPrompt

from modules.installPackage import installPackage
from modules.showPackages import showPackages
from modules.uninstallPackage import uninstallPackage
from modules.updatePackages import updatePackages

user = os.getlogin()

menu_items = ["Install", "Uninstall", "Show installed packages", "Update", "Exit"]

fzf = FzfPrompt()
menu_entry = fzf.prompt(menu_items)


def mainMenu():
    if menu_entry[0] == "Install":
        installPackage()
    elif menu_entry[0] == "Uninstall":
        uninstallPackage()
    elif menu_entry[0] == "Show installed packages":
        showPackages()
    elif menu_entry[0] == "Update":
        updatePackages()
    elif menu_entry[0] == "Exit":
        exit(0)
    else:
        print("Invalid option")


mainMenu()
