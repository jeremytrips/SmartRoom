import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from widget.LabelInput import LabelInput

from widget.modulesetter import ModuleSetter
from serialcom import SerialCom
import serial
from kivy.core.window import Window


class MainLayout(FloatLayout):

    def __init__(self):
        super(MainLayout, self).__init__()

        input_ssid = LabelInput("SSID", 0.85)
        input_password = LabelInput("SSID Password", 0.7)
        input_ip = LabelInput("Server Ip", 0.55)
        input_port = LabelInput("Server port", 0.4)

        connect_button = Button(text='Connect', on_press=self.connect, size_hint=(0.15, 0.1),
                                pos_hint={'x': 0.825, 'y': 0.3})
        close_button = Button(text='Disconnect', on_press=self.close, size_hint=(0.15, 0.1),
                              pos_hint={'x': 0.825, 'y': 0.1})

        send_button = Button(text='Send', on_press=self.send, size_hint=(0.15, 0.1),
                             pos_hint={'x': 0.825, 'y': 0.2})

        self.module_handler = ModuleSetter()

        self.inputs = [input_ssid, input_password, input_ip, input_port]
        for w in self.inputs:
            self.add_widget(w)

        self.add_widget(self.module_handler)
        self.add_widget(connect_button)
        self.add_widget(send_button)
        self.add_widget(close_button)

    def connect(self, value):
        self.module_handler.connect()

    def close(self, *args):
        self.module_handler.close()
        return

    def send(self, *args):
        print("ocouc")


class SerialTest(App):
    Window.clearcolor = (0.5, 0.5, 0.5, 0.5)

    def build(self):
        self.title = "Smart configurator v1.0"
        return MainLayout()


if __name__ == "__main__":
    SerialTest().run()
