import os
from modules.customTable import customTable
from modules.diffInstalled import diffInstalled
from modules.exportToFile import exportToFile
from modules.installDiff import installDiff
from modules.menuTable import menuTable
from modules.packagesMenu import packagesMenu
from modules.searchPackage import searchPackage
user = os.getlogin()

def mainMenu():
    customTable('Main Menu', ['Id', 'Option'], 
                   [
                       ['1', '[green]Pacman'],
                       ['2', '[blue]Yay'],
                       ['3', '[yellow]Search'],
                       ['4', '[red]Exit']
                   ]
                   )
    menu_option = input("[yellow]Enter option: ")
    pacman = True
    if menu_option == '':
        print("[red]Invalid option")
        exit()
    if menu_option == '1':
        pacman = True
    elif menu_option == '2':
        pacman = False
    elif menu_option == '3':
        searchPackage()
    elif menu_option == '4':
        exit(0)
    
    packagesMenu(pacman)

mainMenu()
