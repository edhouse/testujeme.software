import time

class DSLRCamera:
    def __init__(self, name: str):
        self._iso = 100
        self._shutter_speed = round(1/60, 3)
        self._aperture = 2.8
        self._focus_point = (0, 0)
        self.name = name

    def take_photo(self):
        print(f"{self.name}: Taking photo with ISO: {self._iso}, Shutter Speed: {self._shutter_speed}, Aperture: {self._aperture}, Focus Point: {self._focus_point}")
        time.sleep(2)  # Simulate taking a photo

    def auto_adjust(self):
        self._iso = 100
        self._shutter_speed = round(1/120, 3)
        self._aperture = 1.6
        self._focus_point = (100, 100)
        print(f"{self.name}: Auto adjustment done.")
        time.sleep(1)  # Simulate auto adjustment process

    @property
    def iso(self):
        return self._iso

    @iso.setter
    def iso(self, value):
        self._iso = value
        print(f"{self.name}: ISO set to {value}")
        time.sleep(1)  # Simulate setting process

    @property
    def shutter_speed(self):
        return self._shutter_speed

    @shutter_speed.setter
    def shutter_speed(self, value):
        self._shutter_speed = value
        print(f"{self.name}: Shutter speed set to {value}")
        time.sleep(1)  # Simulate setting process

    @property
    def aperture(self):
        return self._aperture

    @aperture.setter
    def aperture(self, value):
        self._aperture = value
        print(f"{self.name}: Aperture set to {value}")
        time.sleep(1)  # Simulate setting process

    @property
    def focus_point(self):
        return self._focus_point

    @focus_point.setter
    def focus_point(self, value):
        self._focus_point = value
        print(f"{self.name}: Focus point set to {value}")
        time.sleep(1)  # Simulate setting process
