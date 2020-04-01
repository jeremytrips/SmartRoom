import time

from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color
from kivy.uix.spinner import Spinner
from serialcom import SerialCom
import threading


class ModuleSetter(FloatLayout):

    def __init__(self):
        super(ModuleSetter, self).__init__()
        self.__port = None
        self.size_hint = (0.5, 0.2)
        self.pos_hint = {'x': 0, 'y': 0}

        self._get_response = threading.Thread(target=self._get_data)

        self.available_port_spinner = Spinner(size_hint=(0.3, 0.2), pos_hint={'x': 0.05, 'y': 0.75},
                                              text="Select port", values=SerialCom.list_port())
        self.available_port_spinner.bind(text=self.set_port)

        self.__serial_port = SerialCom()

        self.__connected = False

        with self.canvas:
            Color(1, 1, 1, 0.3)  # set the colour to red
            self.rect = Rectangle(pos=self.center, size=(self.width / 2, self.height / 2))
            self.bind(pos=self.update_rect,
                      size=self.update_rect)
        self.add_widget(self.available_port_spinner)

    def set_port(self, *args):
        self.__port = args[1]

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def connect(self):
        if self.__port is None:
            #todo
            self.alert()
            return
        self.__serial_port.port = self.__port
        self.__serial_port.send(b"01010101")
        while not self.__serial_port.get_received():
            time.sleep(0.1)
        if self.__serial_port.get_received() == b"01010101":
            self.__connected = True

    def close(self):
        self.__serial_port.close()
        return



"""
    try:
        for data in self.inputs:
            if len(data.get_text_input()) == 0:
                popup = Popup(title='Error',
                              content=Label(text=f"Field not valid.\n({self.port_spinner.text})",
                                            valign='middle'),
                              size_hint=(None, None), size=(400, 200))
                popup.open()
                return
        tmp = self.serial_port.send(self.send_text_input.text, self.action_spinner.text[0])
        self.label.text += f"{tmp}\n"
        self.send_text_input.text = ""
        self.send_text_input.focus = True
    except serial.serialutil.SerialException:
        popup = Popup(title='Error',
                      content=Label(text="Please connect to a device first!"),
                      size_hint=(None, None), size=(400, 400))
        popup.open()
"""