from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

from .layout.modulelist import ModuleList


class MainLayout(FloatLayout):

    def __init__(self):
        super(MainLayout, self).__init__()
