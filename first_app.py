from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        return Builder.load_string("""
MDBoxLayout:
    orientation: 'vertical'
    MDToolbar:
        title: 'JTeam'
        md_bg_color: app.theme_cls.primary_color
    MDLabel:
        text: 'JTeam!'
        halign: 'center'
""")

if __name__ == '__main__':
    MainApp().run()
