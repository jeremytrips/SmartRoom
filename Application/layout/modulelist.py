from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class ModuleList(BoxLayout, Widget):

    def __init__(self):
        super(ModuleList, self).__init__()
        self.orientation = 'horizontal'
         
