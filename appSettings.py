import os
def appSettings():
    SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
    SEARCH_PACMAN_PATH = f"{SCRIPT_PATH}/search_pacman.txt"
    SEARCH_YAY_PATH = f"{SCRIPT_PATH}/search_yay.txt"
    return {
            "SEARCH_PACMAN_PATH": SEARCH_PACMAN_PATH,
            "SEARCH_YAY_PATH": SEARCH_YAY_PATH
            }
