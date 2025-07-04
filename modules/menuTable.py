from rich.console import Console
from rich.table import Table


def menuTable():
    table = Table(title="[green]Choose an option")

    table.add_column("Id")
    table.add_column("Title")

    table.add_row("1)", "[green]Install")
    table.add_row("2)", "[blue]Search in pacman")
    table.add_row("2.1)", "[blue]Search in yay")
    table.add_row("3)", "[magenta]Uninstall")
    table.add_row("4)", "[green]Find throw pacman installed")
    table.add_row("5)", "[green]Find throw yay installed")
    table.add_row("6)", "[yellow]Packages")
    table.add_row("7)", "[magenta]Exit")

    console = Console()
    console.print(table)

    option = float(input("[blue]Choose an option: "))
    return option
