from screens import *


class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "main_scr"
        self.lab = MDLabel(text="hello")
        self.add_widget(self.lab)
