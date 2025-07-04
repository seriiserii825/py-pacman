from modules.saveInstalledPackagesToFiles import saveInstalledPackagesToFiles


def syncDiffWithInstalled():
    choose = input("Do you want to sync diff with installed packages,y/n?: ")
    if choose == "y":
        saveInstalledPackagesToFiles(True)
    else:
        return
