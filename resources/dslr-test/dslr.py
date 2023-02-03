import time

class DSLRCamera:
    def __init__(self):
        self._iso = 100
        self._shutter_speed = 1/60
        self._aperture = 2.8
        self._focus_point = (0, 0)

    def take_photo(self):
        print(f"Taking photo with ISO: {self._iso}, Shutter Speed: {self._shutter_speed}, Aperture: {self._aperture}, Focus Point: {self._focus_point}")
        time.sleep(2)  # Simulate taking a photo

    def auto_adjust(self):
        self._iso = 100
        # self._shutter_speed = 1/120
        self._aperture = 1.6
        self._focus_point = (100, 100)
        print("Auto adjustment done.")
        time.sleep(1)  # Simulate auto adjustment process

    @property
    def iso(self):
        return self._iso

    @iso.setter
    def iso(self, value):
        self._iso = value
        print(f"ISO set to {value}")
        time.sleep(1)  # Simulate setting process

    @property
    def shutter_speed(self):
        return self._shutter_speed

    @shutter_speed.setter
    def shutter_speed(self, value):
        self._shutter_speed = value
        print(f"Shutter speed set to {value}")
        time.sleep(1)  # Simulate setting process

    @property
    def aperture(self):
        return self._aperture

    @aperture.setter
    def aperture(self, value):
        self._aperture = value
        print(f"Aperture set to {value}")
        time.sleep(1)  # Simulate setting process

    @property
    def focus_point(self):
        return self._focus_point

    @focus_point.setter
    def focus_point(self, value):
        self._focus_point = value
        print(f"Focus point set to {value}")
        time.sleep(1)  # Simulate setting process
