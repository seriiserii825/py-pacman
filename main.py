import os
from modules.customTable import customTable
from modules.diffInstalled import diffInstalled
from modules.exportToFile import exportToFile
from modules.installDiff import installDiff
from modules.menuTable import menuTable
from modules.packagesMenu import packagesMenu
user = os.getlogin()

def mainMenu():
    customTable('Main Menu', ['Id', 'Option'], 
                   [
                       ['1', '[green]Pacman'],
                       ['2', '[blue]Yay'],
                       ['3', 'Exit'],
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
        exit(0)
    
    packagesMenu(pacman)

mainMenu()

def menu():
    menu_option = menuTable()
    if menu_option == 1:
        package = input("Enter package name: ")
        os.system(f"sudo pacman -S {package}")
        exportToFile(package)
        menu()
    elif menu_option == 2:
        package = input("Enter package name: ")
        os.system(f"sudo pacman -Ss {package}")
        menu()
    elif menu_option == 2.1:
        package = input("Enter package name: ")
        os.system(f"sudo yay -Ss {package}")
        menu()
    elif menu_option == 3:
        package = input("Enter package name: ")
        os.system(f"sudo pacman -R {package}")
        exportToFile()
        menu()
    elif menu_option == 4:
        package = input("Enter package name, or leave empty: ")
        os.system(f"pacman -Qs | grep {package}")
        menu()
    elif menu_option == 5:
        package = input("Enter package name, or leave empty: ")
        os.system(f"pacman -Qm | grep {package}")
        menu()
    elif menu_option == 6:
        packagesMenu()
        menu()
    elif menu_option == 6.1:
        command = f"pacman -Qe | awk '{{print $1}}' | less"
        os.system(command)
        menu()
    elif menu_option == 6.2:
        diffInstalled()
        menu()
    elif menu_option == 6.3:
        installDiff()
        menu()
    elif menu_option == 7:
        exit(0)
# menu()

