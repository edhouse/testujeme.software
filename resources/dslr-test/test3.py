from dslr import DSLRCamera  # dummy app
from prettytable import PrettyTable
from colorama import Fore, Style

camera1 = DSLRCamera()
camera2 = DSLRCamera()
camera3 = DSLRCamera()

header = ["Camera", "ISO", "Shutter Speed", "Aperture", "Focus Point"]

data_before = [
    ["Camera 1", camera1.iso, camera1.shutter_speed, camera1.aperture, camera1.focus_point],
    ["Camera 2", camera2.iso, camera2.shutter_speed, camera2.aperture, camera2.focus_point],
    ["Camera 3", camera3.iso, camera3.shutter_speed, camera3.aperture, camera3.focus_point],
]

camera1.auto_adjust()
camera2.iso = 700
camera2.focus_point = (0,50)

data_after = [
    ["Camera 1", camera1.iso, camera1.shutter_speed, camera1.aperture, camera1.focus_point],
    ["Camera 2", camera2.iso, camera2.shutter_speed, camera2.aperture, camera2.focus_point],
    ["Camera 3", camera3.iso, camera3.shutter_speed, camera3.aperture, camera3.focus_point],
]


for x, row in enumerate(data_before):
    for y, cell in enumerate(row):
        if data_before[x][y] != data_after[x][y]:
            data_after[x][y] = Fore.RED + str(data_before[x][y]) + Fore.LIGHTBLACK_EX + " -> " + Fore.GREEN + str(data_after[x][y]) + Style.RESET_ALL

table_result = PrettyTable()
table_result.field_names = header
for row in data_after:
    table_result.add_row(row)

print(table_result)
