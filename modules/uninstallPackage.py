import os
from pyfzf.pyfzf import FzfPrompt

from modules.getAllInstalledPackages import getAllInstalledPackages
from modules.saveInstalledPackagesToFiles import saveInstalledPackagesToFiles
fzf = FzfPrompt()
user = os.getlogin()
def uninstallPackage(package_name = None):
    saveInstalledPackagesToFiles()
    packages = getAllInstalledPackages()
    all = packages["all"]
    packages_from_pacman = packages["pacman"]
    if not packages:
        print("[red]No packages to uninstall")
        return
    if (package_name):
        package = [package_name]
    else:
        package = fzf.prompt(all)
    if not package:
        return
    print(f"Uninstalling {package[0]}")
    if package[0] in packages_from_pacman:
        os.system(f"sudo pacman -R {package[0]}")
    else:
        os.system(f"yay -R {package[0]}")
    saveInstalledPackagesToFiles()
