import os
from modules.customTable import customTable
from modules.installPackage import installPackage
from modules.packagesMenu import packagesMenu
from modules.saveInstalledPackagesToFiles import saveInstalledPackagesToFiles
from modules.searchPackage import searchPackage
from modules.uninstallPackage import uninstallPackage
user = os.getlogin()

def mainMenu():
    customTable('Main Menu', ['Id', 'Option'], 
                   [
                       ['1', '[green]Install'],
                       ['2', '[blue]Uninstall'],
                       ['3', '[yellow]Save installed packages to file'],
                       ['4', '[red]Exit']
                   ]
                   )
    menu_option = input("[green]Enter option: ")

    if menu_option == '':
        print("[red]Invalid option")
        exit()
    if menu_option == '1':
       installPackage()
    elif menu_option == '2':
        uninstallPackage()
    elif menu_option == '3':
        saveInstalledPackagesToFiles()
    
    # packagesMenu(pacman)

# def mainMenu():
#     customTable('Main Menu', ['Id', 'Option'], 
#                    [
#                        ['1', '[green]Pacman'],
#                        ['2', '[blue]Yay'],
#                        ['3', '[yellow]Search'],
#                        ['4', '[red]Exit']
#                    ]
#                    )
#     menu_option = input("[yellow]Enter option: ")
#     pacman = True
#     if menu_option == '':
#         print("[red]Invalid option")
#         exit()
#     if menu_option == '1':
#         pacman = True
#     elif menu_option == '2':
#         pacman = False
#     elif menu_option == '3':
#         searchPackage()
#     elif menu_option == '4':
#         exit(0)
#     
#     packagesMenu(pacman)

mainMenu()
