import os

from py_libs.Select import Select

from modules.installPackage import installPackage
from modules.showPackages import showPackages
from modules.uninstallPackage import uninstallPackage
from modules.updatePackages import updatePackages

user = os.getlogin()

menu_items = ["Install", "Uninstall", "Show installed packages", "Update", "Exit"]

menu_entry = Select.select_fzf_one(menu_items)


def mainMenu():
    if menu_entry == "Install":
        installPackage()
    elif menu_entry == "Uninstall":
        uninstallPackage()
    elif menu_entry == "Show installed packages":
        showPackages()
    elif menu_entry == "Update":
        updatePackages()
    elif menu_entry == "Exit":
        exit(0)
    else:
        print("Invalid option")


mainMenu()
