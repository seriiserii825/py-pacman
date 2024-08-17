import os
from pyfzf.pyfzf import FzfPrompt

from modules.exportToFile import exportToFile
from modules.removePackageFromFile import removePackageFromFile
fzf = FzfPrompt()
user = os.getlogin()
def uninstallPackage(pacman = True, prop_package = ''):
    file_name = "pacman_list.txt" if pacman else "yay_list.txt"
    file_path = f"/home/{user}/xubuntu/{file_name}"
    if prop_package:
        package = prop_package
    else:
        with open(file_path, "r") as f:
            lines = f.readlines()
        # remove the newline character
        lines = [line.strip() for line in lines]
        package = fzf.prompt(lines)[0]
        if not package:
            return
    if pacman:
        os.system(f"sudo pacman -R {package}")
        removePackageFromFile(file_path, package)
    else:
        os.system(f"yay -R {package}")
        removePackageFromFile(file_path, package)
    print(f"{package} has been uninstalled")
    exportToFile(pacman)
