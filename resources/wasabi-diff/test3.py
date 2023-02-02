from dslr import DSLRCamera  # dummy app
import webbrowser
import difflib
from wasabi import table

camera1 = DSLRCamera()
camera2 = DSLRCamera()
camera3 = DSLRCamera()

before = [
    ("Camera 1", camera1.iso, camera1.shutter_speed, camera1.aperture, camera1.focus_point),
    ("Camera 2", camera2.iso, camera2.shutter_speed, camera2.aperture, camera2.focus_point),
    ("Camera 3", camera3.iso, camera3.shutter_speed, camera3.aperture, camera3.focus_point),
    ]
table_before = table(before, header=("Camera", "ISO", "Shutter Speed", "Aperture", "Focus Point"), divider=True)

camera1.auto_adjust()
camera2.iso = 700
camera2.focus_point = (0,50)

after = [
    ("Camera 1", camera1.iso, camera1.shutter_speed, camera1.aperture, camera1.focus_point),
    ("Camera 2", camera2.iso, camera2.shutter_speed, camera2.aperture, camera2.focus_point),
    ("Camera 3", camera3.iso, camera3.shutter_speed, camera3.aperture, camera3.focus_point),
    ]
table_after = table(after, header=("Camera", "ISO", "Shutter Speed", "Aperture", "Focus Point"), divider=True)


diff = difflib.HtmlDiff(tabsize=2).make_file(table_before.splitlines(), table_after.splitlines(), fromdesc='Before', todesc='After', numlines=3,context=True)
file = open('diff.html', 'w+', encoding='utf8')
file.write(diff)
file.close()
webbrowser.open('diff.html')