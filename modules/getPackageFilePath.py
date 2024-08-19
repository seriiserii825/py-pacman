import os
user = os.getlogin()
def getPackageFilePath(pacman):
    file_name = "pacman_list.txt" if pacman else "yay_list.txt"
    return f"/home/{user}/xubuntu/{file_name}"
