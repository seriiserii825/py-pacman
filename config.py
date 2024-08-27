import os
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
class CONFIG:
    SEARCH_PACMAN_PATH = f"{SCRIPT_PATH}/search_pacman.txt"
    SEARCH_YAY_PATH = f"{SCRIPT_PATH}/search_yay.txt"
    INSTALLED_PACMAN_PATH = f"{SCRIPT_PATH}/installed_pacman.txt"
    INSTALLED_YAY_PATH = f"{SCRIPT_PATH}/installed_yay.txt"
    def __init__(self):
        pass
