import Menu
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, NumericProperty

class MyApp(App):
    TITLE = "Log Laws"
    def build(self):
        global sm
        sm.add_widget(Menu.Menu(name="Menu"))
        Menu.sm = sm
        return sm

if __name__ == '__main__':
    sm = ScreenManager()
    MyApp().run()