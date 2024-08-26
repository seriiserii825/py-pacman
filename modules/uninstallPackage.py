import os
from pyfzf.pyfzf import FzfPrompt

from modules.getPackageFilePath import getPackageFilePath
from modules.removePackageFromFile import removePackageFromFile
fzf = FzfPrompt()
user = os.getlogin()
def uninstallPackage():
    packages_from_yay = []
    with open(getPackageFilePath(True), "r") as f:
        lines = f.readlines()
    # remove the newline character
    lines = [line.strip() for line in lines]
    packages_from_pacman = lines
    with open(getPackageFilePath(False), "r") as f:
        lines = f.readlines()
    # remove the newline character
    lines = [line.strip() for line in lines]
    packages_from_yay = lines
    packages = packages_from_pacman + packages_from_yay
    if not packages:
        print("[red]No packages to uninstall")
        return
    package = fzf.prompt(packages)
    if not package:
        return
    print(f"Uninstalling {package[0]}")
    if package[0] in packages_from_pacman:
        os.system(f"sudo pacman -R {package[0]}")
        removePackageFromFile(getPackageFilePath(True), package[0])
    else:
        os.system(f"yay -R {package[0]}")
        removePackageFromFile(getPackageFilePath(False), package[0])
