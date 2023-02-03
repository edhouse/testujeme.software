from dslr import DSLRCamera  # dummy app
from prettytable import PrettyTable

camera1 = DSLRCamera()
camera2 = DSLRCamera()
camera3 = DSLRCamera()

table_before = PrettyTable()
table_before.field_names = ["Camera", "ISO", "Shutter Speed", "Aperture", "Focus Point"]
table_before.add_row(["Camera 1", camera1.iso, camera1.shutter_speed, camera1.aperture, camera1.focus_point])
table_before.add_row(["Camera 2", camera2.iso, camera2.shutter_speed, camera2.aperture, camera2.focus_point])
table_before.add_row(["Camera 3", camera3.iso, camera3.shutter_speed, camera3.aperture, camera3.focus_point])

print('Before:')
print(table_before)

camera1.auto_adjust()
camera2.iso = 700
camera2.focus_point = (0,50)

table_after = PrettyTable()
table_after.field_names = ["Camera", "ISO", "Shutter Speed", "Aperture", "Focus Point"]
table_after.add_row(["Camera 1", camera1.iso, camera1.shutter_speed, camera1.aperture, camera1.focus_point])
table_after.add_row(["Camera 2", camera2.iso, camera2.shutter_speed, camera2.aperture, camera2.focus_point])
table_after.add_row(["Camera 3", camera3.iso, camera3.shutter_speed, camera3.aperture, camera3.focus_point])

print('After:')
print(table_after)
