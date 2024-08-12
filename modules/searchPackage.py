import os
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
def searchPackage(package_name = ''):
    if package_name != '':
        package = package_name
    else:
        package = input("Enter package name: ")
    where_to_search = Prompt.ask("Where to search", choices=["Pacman", "Yay"], default="Pacman")
    if where_to_search == "Pacman":
        print(Panel("Searching in pacman..."))
        os.system(f"pacman -Ss {package}")
    else:
        print(Panel("Searching in yay..."))
        os.system(f"yay -Ss {package}")
    search_again = Prompt.ask("Search again?", choices=["Yes", "No"], default="No")
    if search_again == "Yes":
        searchPackage(package)
    else:
        print("Goodbye!")
        exit()
