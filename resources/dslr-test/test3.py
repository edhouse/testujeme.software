from dslr import DSLRCamera  # dummy app
from tables_diff import tables_diff

# test script
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

table_result = tables_diff(data_before, data_after, header)
print('Test result')
print(table_result)