def customTable(title = '', columns = [], rows = []):
    from rich.console import Console
    from rich.table import Table

    if title == '':
        table = Table(title=title)
    else:
        table = Table()

    if len(columns) > 0:
        for column in columns:
            table.add_column(column)

    if len(rows) > 0:
        for row in rows:
            if type(row) == list:
                table.add_row(*row)
            else:
                table.add_row(row)
    else:
        table.add_row("No data")

    console = Console()
    console.print(table)

