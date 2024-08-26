import os
from modules.customTable import customTable
from modules.installPackage import installPackage
from modules.packagesMenu import packagesMenu
from modules.searchPackage import searchPackage
user = os.getlogin()

def mainMenu():
    customTable('Main Menu', ['Id', 'Option'], 
                   [
                       ['1', '[green]Install'],
                       ['2', '[blue]Uninstall'],
                       ['4', '[red]Exit']
                   ]
                   )
    menu_option = input("[green]Enter option: ")

    if menu_option == '':
        print("[red]Invalid option")
        exit()
    if menu_option == '1':
       installPackage()
    
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
