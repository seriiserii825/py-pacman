import os
from modules.customTable import customTable
from modules.installDiff import installDiff
from modules.installPackage import installPackage
from modules.saveInstalledPackagesToFiles import saveInstalledPackagesToFiles
from modules.showPackages import showPackages
from modules.syncDiffWithInstalled import syncDiffWithInstalled
from modules.uninstallPackage import uninstallPackage
user = os.getlogin()

def mainMenu():
    customTable('Main Menu', ['Id', 'Option'], 
                   [
                       ['1', '[green]Install'],
                       ['2', '[blue]Uninstall'],
                       ['3', '[yellow]Show installed packages'],
                       ['4', '[green]Install diff packages'],
                       ['5', '[red]Sync diff with installed packages'],
                       ['6', '[red]Exit']
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
        showPackages()
    elif menu_option == '4':
        installDiff()
    elif menu_option == '5':
        syncDiffWithInstalled()
mainMenu()
