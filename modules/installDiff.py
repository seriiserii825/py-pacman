import os
from rich import print

from modules.getAllInstalledPackages import getAllInstalledPackages
from modules.installPackage import installPackage
from modules.saveInstalledPackagesToFiles import saveInstalledPackagesToFiles
from modules.uninstallPackage import uninstallPackage
user = os.getlogin()
from config import CONFIG
def installDiff():
    packages = getAllInstalledPackages()
    all = packages["all"]
    print(f"[green]Total installed packages: {len(all)}")
    with open(CONFIG.DIFF_FILE_PATH, "r") as f:
        lines = f.readlines()
    diff_packages = [line.strip() for line in lines]
    print(f"[green]Total diff packages: {len(diff_packages)}")
    # get diff from all and diff_packages
    diff_packages_from_installed = list(set(all) - set(diff_packages))
    if not diff_packages_from_installed:
        print("[red]No diff packages from installed")
    else:
        print(f"Packages to uninstall: {diff_packages_from_installed}")
        choose = input("Do you want to uninstall? [y/n]: ")
        if choose == "y":
            for package in diff_packages_from_installed:
                agree = input(f"Uninstall {package}? [y/n]: ")
                if agree == "y":
                    uninstallPackage(package)
    diff_packages_from_diff_file = list(set(diff_packages) - set(all))
    if not diff_packages_from_diff_file:
        print("[red]No diff packages from diff file")
    else:
        print(f"Packages to install: {diff_packages_from_diff_file}")
        choose = input("Do you want to install these packages? [y/n]: ")
        if choose == "y":
            for package in diff_packages_from_diff_file:
                agree = input(f"Install {package}? [y/n]: ")
                if agree == "y":
                    installPackage(package)
    
    saveInstalledPackagesToFiles()
