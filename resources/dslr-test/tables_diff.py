from prettytable import PrettyTable
from colorama import Fore, Style

# diff function
def tables_diff(data_before, data_after, header):
    table_result = PrettyTable()
    table_result.field_names = header

    for x, row in enumerate(data_before):
        for y, cell in enumerate(row):
            if data_before[x][y] != data_after[x][y]:
                data_after[x][y] = Fore.RED + str(data_before[x][y]) + Fore.LIGHTBLACK_EX + " -> " + Fore.GREEN + str(data_after[x][y]) + Style.RESET_ALL

    for row in data_after:
        table_result.add_row(row)
    
    return table_result