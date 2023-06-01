from dslr import DSLRCamera  # dummy app
from prettytable import PrettyTable

# test script
camera1 = DSLRCamera("Canon")
camera2 = DSLRCamera("Nikon")
camera3 = DSLRCamera("Sony")

table_before = PrettyTable()
table_before.field_names = ["Camera", "ISO", "Shutter Speed", "Aperture", "Focus Point"]
table_before.add_row([camera1.name, camera1.iso, camera1.shutter_speed, camera1.aperture, camera1.focus_point])
table_before.add_row([camera2.name, camera2.iso, camera2.shutter_speed, camera2.aperture, camera2.focus_point])
table_before.add_row([camera3.name, camera3.iso, camera3.shutter_speed, camera3.aperture, camera3.focus_point])

print('Before:')
print(table_before)

print()

camera1.auto_adjust()
camera2.iso = 700
camera2.focus_point = (0,50)

print()

table_after = PrettyTable()
table_after.field_names = ["Camera", "ISO", "Shutter Speed", "Aperture", "Focus Point"]
table_after.add_row([camera1.name, camera1.iso, camera1.shutter_speed, camera1.aperture, camera1.focus_point])
table_after.add_row([camera2.name, camera2.iso, camera2.shutter_speed, camera2.aperture, camera2.focus_point])
table_after.add_row([camera3.name, camera3.iso, camera3.shutter_speed, camera3.aperture, camera3.focus_point])

print()
print('After:')
print(table_after)