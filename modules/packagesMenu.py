import os
from modules.customTable import customTable
from modules.diffInstalled import diffInstalled
from modules.exportToFile import exportToFile
from modules.installDiff import installDiff
from modules.installPackage import installPackage
from modules.menuTable import menuTable
from modules.searchPackage import searchPackage
from modules.showPackages import showPackages
from modules.uninstallPackage import uninstallPackage
user = os.getlogin()

def packagesMenu(pacman):
    table_column = 'Pacman' if pacman else 'Yay'
    customTable('Packages Menu', ['Id', table_column], 
                   [
                       ['1. ', '[blue]Install package'],
                       ['2. ', '[green]Show installed packages'],
                       ['3. ', '[yellow]All installed to file'],
                       ['4. ', '[yellow]Diff packages'],
                       ['5. ', '[blue]View local file'],
                       ['6. ', '[red]Remove package'],
                       ['7. ', '[red]Exit'],
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
        showPackages(pacman)
        packagesMenu(pacman)
    elif menu_option == '3':
        exportToFile(pacman)
        packagesMenu(pacman)
    elif menu_option == '4':
        diffInstalled(pacman)
        packagesMenu(pacman)
    elif menu_option == '5':
        file_name = "pacman_list.txt" if pacman else "yay_list.txt"
        file_path = f"/home/{user}/xubuntu/{file_name}"
        os.system(f"less {file_path}")
        packagesMenu(pacman)
    elif menu_option == '6':
        uninstallPackage(pacman)
        packagesMenu(pacman)
    elif menu_option == 7:
        exit(0)

