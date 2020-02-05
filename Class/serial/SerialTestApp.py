import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

from .serialcommunication import SerialCommunication


class MainLayout(FloatLayout):

    def __init__(self):
        super(MainLayout, self).__init__()
        self.label = TextInput(readonly=True, size_hint=(0.8, 0.9), pos_hint={'y': 0.1})

        self.send_text_input = TextInput(size_hint=(0.5, 0.05), pos_hint={'x': 0.1, 'y': 0.025}, multiline=False,
                                         on_text_validate=self.send_data)

        self.port_spinner = Spinner(size_hint=(0.15, 0.1), pos_hint={'x': 0.825, 'y': 0.7})

        self.add_widget(self.send_text_input)
        self.add_widget(self.label)
        self.add_widget(self.port_spinner)

    def send_data(self, obj):
        print(obj.text)
        self.label.text += f"{obj.text}\n"
        obj.text = ""
        self.send_text_input.focus = True


class SerialTest(App):

    def build(self):
        return MainLayout()


if __name__ =="__main__":
    SerialTest().run()