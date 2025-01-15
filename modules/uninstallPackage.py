import os
from pyfzf.pyfzf import FzfPrompt
from rich import print

from classes.Package import Package
fzf = FzfPrompt()
user = os.getlogin()
def uninstallPackage():
    packages = Package()
    packages.getPackagesFromPacmanFile()
    packages_from_pacman = packages.getPacmanPackages()
    packages.getPackagesFromYayFile()
    packages_from_yay = packages.getYayPackages()
    all_packages = packages_from_pacman + packages_from_yay
    package_name = fzf.prompt(all_packages)[0]
    print(f"package_name: {package_name}")
    if package_name in packages_from_pacman:
        os.system(f"sudo pacman -R {package_name}")
        print(f"[green]Uninstalled {package_name} with pacman")
        packages.removePackageFromPacmanFile(package_name)
    else:
        os.system(f"yay -R {package_name}")
        print(f"[green]Uninstalled {package_name} with yay")
        packages.removePackageFromYayFile(package_name)
