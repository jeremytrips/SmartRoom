import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from widget.LabelInput import LabelInput

from widget.modulesetter import ModuleSetter
from kivy.core.window import Window


class MainLayout(FloatLayout):

    def __init__(self):
        super(MainLayout, self).__init__()

        input_ssid = LabelInput("SSID", 0.85)
        input_password = LabelInput("SSID Password", 0.7)
        input_ip = LabelInput("Server Ip", 0.55)
        input_port = LabelInput("Server port", 0.4)

        send_button = Button(text='Send', size_hint=(0.15, 0.1), on_press=self.write_module,
                             pos_hint={'x': 0.825, 'y': 0.2})

        self.module_handler = ModuleSetter()

        self.inputs = [input_ssid, input_password, input_ip, input_port]
        for w in self.inputs:
            self.add_widget(w)

        self.add_widget(self.module_handler)
        self.add_widget(send_button)

    def write_module(self, *args):
        if self.module_handler.is_connected():
            data = dict()
            data["s"] = self.inputs[0].get_text_input()
            data["p"] = self.inputs[1].get_text_input()
            data["i"] = self.inputs[2].get_text_input()
            data["o"] = self.inputs[3].get_text_input()
            self.module_handler.write_module(data)
        else:
            Popup(title='Warning',
                  content=Label(text='Module is not connected'),
                  size_hint=(0.5, 0.5)).open()


class SerialTest(App):
    Window.clearcolor = (0.5, 0.5, 0.5, 0.5)

    def build(self):
        self.title = "Smart configurator v1.0"
        return MainLayout()


if __name__ == "__main__":
    SerialTest().run()
