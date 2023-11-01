"""Navigation panel with screens"""

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.svg import Window
from kivymd.app import MDApp


Window.size = (360, 600)

# the main screen of the application
class HomeWindow(Screen):
    """The main screen of the application"""
    pass


# second screen of the application
class ScreenPlay(Screen):
    """Second screen of the application"""
    pass


# the third screen of the application
class ScreenMore(Screen):
    """The third screen of the application"""
    pass


# manager of screen
class ScreenManager(ScreenManager):
    """Manager of screen"""
    def switch_screen(self, screen_name):
        self.current = screen_name


class MainApp(MDApp):
    """Main class for run application"""
    def build(self):
        self.screen_manager = Builder.load_file('main.kv')
        return self.screen_manager

if __name__ == '__main__':
    MainApp().run()
