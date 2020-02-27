import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

from serialcom import SerialCom 


class MainLayout(FloatLayout):

    def __init__(self):
        super(MainLayout, self).__init__()
        self.label = TextInput(readonly=True, size_hint=(0.8, 0.9), pos_hint={'y': 0.1})

        self.send_text_input = TextInput(size_hint=(0.5, 0.05), pos_hint={'x': 0.1, 'y': 0.025}, multiline=False,
                                         on_text_validate=self.send)

        self.action_spinner = Spinner(size_hint=(0.15, 0.1), pos_hint={'x': 0.825, 'y': 0.5}, text="action",
                                    values=['ssid', 'password', 'ip', 'port'])

        self.port_spinner = Spinner(size_hint=(0.15, 0.1), pos_hint={'x': 0.825, 'y': 0.7}, text="Port",
                                    values=SerialCom.list_port())

        connect_button  = Button(text='Connect', on_press=self.connect, size_hint=(0.15, 0.1),
                                    pos_hint={'x': 0.825, 'y': 0.3})
    
        send_button  = Button(text='Send', on_press=self.send, size_hint=(0.15, 0.1),
                                pos_hint={'x': 0.825, 'y': 0.2})

        self.serial_port = SerialCom()            
    
        self.add_widget(self.send_text_input)
        self.add_widget(self.label)
        self.add_widget(self.port_spinner)
        self.add_widget(self.action_spinner)
        self.add_widget(connect_button)
        self.add_widget(send_button)

        self.com = SerialCom()

    def connect(self, value):
        self.serial_port.port = self.port_spinner.text

    def send(self, obj):
        tmp = self.serial_port.send(self.send_text_input.text, self.action_spinner.text[0])
        self.label.text += f"{tmp}\n"
        obj.text = ""
        self.send_text_input.focus = True


class SerialTest(App):

    def build(self):
        return MainLayout()


if __name__ == "__main__":
    SerialTest().run()
