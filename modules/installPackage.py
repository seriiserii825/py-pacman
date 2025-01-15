import os

# from modules.searchPackage import searchPackage
# from config import CONFIG
# PACMAN_SEARCH_PATH = CONFIG.SEARCH_PACMAN_PATH
# YAY_SEARCH_PATH = CONFIG.SEARCH_YAY_PATH
# from pyfzf.pyfzf import FzfPrompt
# fzf = FzfPrompt()
# def getPackageByName(package_file):
#     packages = open(package_file, "r").read().split("\n")
#     package_name = fzf.prompt(packages)
#     package_name = package_name[0].split(" ")[0]
#     package_name = package_name.split("/")[1]
#     return package_name

def installPackage(package = None):
    pass
    # searchPackage(package)
    # choose = input("Install in pacman or yay? (p/y): ")
    # if choose == "p":
    #     package_name = getPackageByName(PACMAN_SEARCH_PATH)
    #     command = f"sudo pacman -S --noconfirm {package_name}"
    #     os.system(command)
    # elif choose == "y":
    #     if package:
    #         package_name = package
    #     else:
    #         package_name = getPackageByName(YAY_SEARCH_PATH)
    #     command = f"yay -S {package_name}"
    #     os.system(command)
    # else:
    #     print("Invalid input!")
    #     return
