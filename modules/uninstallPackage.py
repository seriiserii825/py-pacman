import os
from pyfzf.pyfzf import FzfPrompt

from config import CONFIG
from modules.saveInstalledPackagesToFiles import saveInstalledPackagesToFiles
fzf = FzfPrompt()
user = os.getlogin()
def uninstallPackage():
    saveInstalledPackagesToFiles()
    with open(CONFIG.INSTALLED_PACMAN_PATH, "r") as f:
        lines = f.readlines()
    # remove the newline character
    lines = [line.strip() for line in lines]
    packages_from_pacman = lines

    with open(CONFIG.INSTALLED_YAY_PATH) as f:
        lines = f.readlines()
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
    else:
        os.system(f"yay -R {package[0]}")
