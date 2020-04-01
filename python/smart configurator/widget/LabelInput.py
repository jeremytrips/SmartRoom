from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class LabelInput(FloatLayout, Widget):

    def __init__(self, label_text, _y):
        super(LabelInput, self).__init__()
        self.pos_hint = {'x': 0.05, 'y': _y}
        self.size_hint = (0.7, 0.1)
        label = Label(text=f"{label_text}: ", pos_hint={'x': -0.3, 'y': 0.5}, size_hint=(1, 0.5),
                      markup=True, halign='left', text_size=(200, None))
        self.__text_input = TextInput(pos_hint={'x': 0.0, 'y': 0.0}, size_hint=(1, 0.5), multiline=False)

        self.add_widget(label)
        self.add_widget(self.__text_input)

    def get_text_input(self):
        return self.__text_input.text


