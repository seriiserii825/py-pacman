import os
from modules.customTable import customTable
from modules.diffInstalled import diffInstalled
from modules.exportToFile import exportToFile
from modules.installDiff import installDiff
from modules.installPackage import installPackage
from modules.menuTable import menuTable
from modules.showPackages import showPackages
user = os.getlogin()

def packagesMenu(pacman):
    table_column = 'Pacman' if pacman else 'Yay'
    customTable('Packages Menu', ['Id', table_column], 
                   [
                       ['1. ', '[blue]Install package'],
                       ['2. ', '[green]Show installed packages'],
                       ['3. ', 'Exit'],
                       ]
                   )
    menu_option = input("Enter option: ")
    if menu_option == '':
        print("Invalid option")
        exit()
    if menu_option == '1':
        installPackage(pacman)
        packagesMenu(pacman)
    elif menu_option == '2':
        showPackages(False)
    elif menu_option == 7:
        exit(0)

