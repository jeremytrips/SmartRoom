import time

from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

from serialcom import SerialCom
import threading


class ModuleSetter(FloatLayout):

    def __init__(self):
        super(ModuleSetter, self).__init__()
        with self.canvas:
            Color(1, 1, 1, 0.3)  # set the colour to red
            self.rect = Rectangle(pos=self.center, size=(self.width / 2, self.height / 2))
            self.bind(pos=self.update_rect,
                      size=self.update_rect)

        self.__data_to_write = dict()
        self.__port = None
        self.size_hint = (0.5, 0.2)
        self.pos_hint = {'x': 0, 'y': 0}

        self._connect_thread = threading.Thread(target=self.connect)

        self.available_port_spinner = Spinner(size_hint=(0.3, 0.2), pos_hint={'x': 0.05, 'y': 0.75},
                                              text="Select port", values=SerialCom.list_port())
        self.available_port_spinner.bind(text=self.set_port)

        self.state_label = Label(text="[color=ff0000]Not connected[/color]", markup=True, halign='center')

        self.__serial_port = SerialCom()

        self.__connected = False

        self.write_thread = threading.Thread(target=self.write_module_thread)

        self.connect_button = Button(text='Connect', on_press=self.connect_thread, size_hint=(0.3, 0.1),
                                     pos_hint={'x': 0.65, 'y': 0.1})

        self.add_widget(self.connect_button)
        self.add_widget(self.available_port_spinner)
        self.add_widget(self.state_label)

    def is_connected(self):
        return self.__connected

    def write_module(self, data):
        self.__data_to_write = data
        print(self.__data_to_write)
        self.write_thread.start()

    def write_module_thread(self):
        i = 0
        for key, value in self.__data_to_write.items():
            self.state_label.text = f"Writing data {i}/4"
            self.__serial_port.write(value, key)
            i += 1
            time.sleep(0.2)

    def set_port(self, *args):
        self.__port = args[1]

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def connect_thread(self, *args):
        if not self.__connected:
            self._connect_thread.start()
        else:
            self.__serial_port.close()
            self.remove_widget(self.connect_button)
            self.state_label.text = "[color=ff0000]Disconnected[/color]"

    def connect(self):
        if not self.__connected:
            if self.__port is None:
                #todo
                self.alert()
                return
            self.state_label.text = "[color=ffa500]Connecting[/color]"
            self.__serial_port.port = self.__port
            time.sleep(3)
            self.__serial_port.write(b'U')
            rcv = self.__serial_port.receive()
            print(f"rcv = {rcv}")
            if rcv == -1:
                self.state_label.text = "[color=ff0000]Error\nDid not get response from device[/color]"
                return
            self.state_label.text = "[color=00ff00]Connected[/color]"
            self.__connected = True
            self.connect_button.text = "Disconnect"

