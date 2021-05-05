import sounddevice as sd
import numpy as np
from phue import Bridge
from rgbxy import Converter, GamutC
from webcolors import name_to_rgb


class Lamp:
    """Class which targets one hue lamp"""
    def __init__(self, lamp_id, bridge_ip):
        """Connection to Bridge and initialize color converter

        :param lamp_id: ID of lamp being targeted
        :type: int
        """
        self.id = lamp_id
        self.b = Bridge(bridge_ip)
        self.b.connect()
        self.converter = Converter(GamutC)
        self.lamp = self.b.get_light(self.id)

    def toggle_active(self):
        """Toggles active state of lamp

        :return: None
        """
        self.b.set_light(self.id, "on", not self.b.get_light(self.id, "on"))

    def toggle_colorloop(self):
        """Toggles colorloop of lamp

        :return: None
        """
        if self.b.get_light(self.id, "effect") == "none":
            self.b.set_light(self.id, "effect", "colorloop")
        else:
            self.b.set_light(self.id, "effect", "none")

    def set_brightness(self, brightness):
        """Set brightness of lamp

        :param brightness: value in range 0-254
        :type: int
        :return: None
        """
        self.b.set_light(self.id, 'bri', brightness)

    def set_color_by_rgb(self, red, blue, green):
        """Set color of lamp via rgb values

        :param red: red proportion (0-255)
        :type: int
        :param blue: blue proportion (0-255)
        :type: int
        :param green: green proportion (0-255)
        :type: int
        :return: None
        """
        color = self.converter.rgb_to_xy(red, blue, green)
        self.b.set_light(self.id, "xy", color)

    def set_color_by_name(self, name):
        """Set color of lamp via name

        :param name: in css3 format
        :type: str
        :return: None
        """
        red, blue, green = name_to_rgb(name, spec='css3')
        self.set_color_by_rgb(red, blue, green)

    def get_input_devices(self):
        """Get ID's of input devices to choose correct one

        :return: All devices
        """
        return sd.query_devices()

    def __audio_callback(self, indata, frames, timer, status):
        """Get Audio callback from InputStream and set brightness

        :param indata: audio data
        :type: np.array
        :param frames: audio frames
        :param timer: audio time
        :param status: audio status
        :return: None
        """
        volume = int(np.linalg.norm(indata) * 10)
        self.set_brightness(volume*2)

    def brightness_by_audio(self, device_id, duration):
        """Set Brightness by audio volume

        :param duration: Duration of brightness by audio
        :param device_id: ID of input device
        :return: None
        """
        duration = duration*1000
        sd.default.device = device_id
        with sd.InputStream(callback=self.__audio_callback):
            sd.sleep(duration)
