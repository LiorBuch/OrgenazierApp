import time

import trio
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager

from screens import *
from screens.main_screen import MainScreen


class LoadingScreen(Screen):
    def __init__(self, screen_manager, **kw):
        super().__init__(**kw)
        self.screen_manager: Type[ScreenManager] = screen_manager
        self.name = "loading_scr"
        self.main_layout = BoxLayout()
        self.greet_label = MDLabel(text="hello there")
        self.progress_bar = ProgressBar(value=50)
        self.main_layout.add_widget(self.greet_label)
        self.main_layout.add_widget(self.progress_bar)

    def on_enter(self, *args):
        self.start_loading()

    def start_loading(self):
        main_screen = MainScreen()
        self.screen_manager.add_widget(main_screen)
        print(self.screen_manager.screens)
        self.screen_manager.current = "main_scr"
