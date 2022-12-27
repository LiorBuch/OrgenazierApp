from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
import trio
from screens.loading_screen import LoadingScreen


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = ScreenManager()
        self.loading_screen = None

    def build(self):
        self.loading_screen = LoadingScreen(self.sm)
        self.sm.add_widget(self.loading_screen)
        self.sm.current = "loading_scr"
        return self.sm


async def run_main():
    MainApp().run()


if __name__ == '__main__':
    trio.run(run_main)
