import os
from modules.diffInstalled import diffInstalled
from modules.exportToFile import exportToFile
from modules.installDiff import installDiff
from modules.menuTable import menuTable
user = os.getlogin()

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
        exportToFile()
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
menu()

