from classes.Package import Package


def installDiff():
    packages = Package()
    package_type = input("Show pacman or yay packages? (p/y): ")
    if package_type == "p":
        packages.getPackagesFromDiffPacmanFile()
        packages.installDiffPacmanPackages()
    elif package_type == "y":
        packages.getPackagesFromDiffPacmanFile()
        packages.installDiffYayPackages()
