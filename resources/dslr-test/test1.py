from dslr import DSLRCamera # dummy app

camera1 = DSLRCamera()
camera2 = DSLRCamera()
camera3 = DSLRCamera()

print('Before:')

print(f'camera1.iso: {camera1.iso}')
print(f'camera1.shutter_speed: {camera1.shutter_speed}')
print(f'camera1.aperture: {camera1.aperture}')
print(f'camera1.focus_point: {camera1.focus_point}')

print(f'camera2.iso: {camera2.iso}')
print(f'camera2.shutter_speed: {camera2.shutter_speed}')
print(f'camera2.aperture: {camera2.aperture}')
print(f'camera2.focus_point: {camera2.focus_point}')

print(f'camera3.iso: {camera3.iso}')
print(f'camera3.shutter_speed: {camera3.shutter_speed}')
print(f'camera3.aperture: {camera3.aperture}')
print(f'camera3.focus_point: {camera3.focus_point}')

camera1.auto_adjust()
camera2.iso = 700
camera2.focus_point = (0,50)

print('After:')

print(f'camera1.iso: {camera1.iso}')
print(f'camera1.shutter_speed: {camera1.shutter_speed}')
print(f'camera1.aperture: {camera1.aperture}')
print(f'camera1.focus_point: {camera1.focus_point}')

print(f'camera2.iso: {camera2.iso}')
print(f'camera2.shutter_speed: {camera2.shutter_speed}')
print(f'camera2.aperture: {camera2.aperture}')
print(f'camera2.focus_point: {camera2.focus_point}')

print(f'camera3.iso: {camera3.iso}')
print(f'camera3.shutter_speed: {camera3.shutter_speed}')
print(f'camera3.aperture: {camera3.aperture}')
print(f'camera3.focus_point: {camera3.focus_point}')