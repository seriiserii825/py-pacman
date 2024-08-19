import os
user = os.getlogin()
def getIgnoredPackagesList():
    packages = []
    file_path = f"/home/{user}/xubuntu/ignored_packages.txt"
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            packages.append(line)
    return packages

