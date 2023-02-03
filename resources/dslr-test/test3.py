from dslr import DSLRCamera  # dummy app
from prettytable import PrettyTable
from colorama import Fore, Style

camera1 = DSLRCamera("Canon")
camera2 = DSLRCamera("Nikon")
camera3 = DSLRCamera("Sony")

header = ["Camera", "ISO", "Shutter Speed", "Aperture", "Focus Point"]

data_before = [
    [camera1.name, camera1.iso, camera1.shutter_speed, camera1.aperture, camera1.focus_point],
    [camera2.name, camera2.iso, camera2.shutter_speed, camera2.aperture, camera2.focus_point],
    [camera3.name, camera3.iso, camera3.shutter_speed, camera3.aperture, camera3.focus_point],
]

print()
camera1.auto_adjust()
camera2.iso = 700
camera2.focus_point = (0,50)
print()

data_after = [
    [camera1.name, camera1.iso, camera1.shutter_speed, camera1.aperture, camera1.focus_point],
    [camera2.name, camera2.iso, camera2.shutter_speed, camera2.aperture, camera2.focus_point],
    [camera3.name, camera3.iso, camera3.shutter_speed, camera3.aperture, camera3.focus_point],
]


for x, row in enumerate(data_before):
    for y, cell in enumerate(row):
        if data_before[x][y] != data_after[x][y]:
            data_after[x][y] = Fore.RED + str(data_before[x][y]) + Fore.LIGHTBLACK_EX + " -> " + Fore.GREEN + str(data_after[x][y]) + Style.RESET_ALL

table_result = PrettyTable()
table_result.field_names = header
for row in data_after:
    table_result.add_row(row)

print('Test result')
print(table_result)
