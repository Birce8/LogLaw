from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math
from kivy.uix.popup import Popup

class Menu(FloatLayout):

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.cols = 2
        title=Label(text='Logarithmic Laws',pos=(-125,220))
        title.font_size = '40dp'
        self.add_widget(title)
        first = Button(pos_hint={'x': .1, 'center_y': .7}, size_hint=(.5, .1),text= 'Log_B(MN)=Log_B(M)+Log_B(N)')
        self.add_widget(first)
        second = Button(pos_hint={'x': .1, 'center_y': .6}, size_hint=(.5, .1),text= 'Log_B(M/N)=Log_B(M)-Log_B(N)')
        self.add_widget(second)
        third = Button(pos_hint={'x': .1, 'center_y': .5}, size_hint=(.5, .1),text= 'Log_B(M^R)=RLog_B(M)')
        self.add_widget(third)
        fourth = Button(pos_hint={'x': .1, 'center_y': .4}, size_hint=(.5, .1),text= 'Log_B(1)=0')
        self.add_widget(fourth)
        fifth= Button(pos_hint={'x': .1, 'center_y': .3}, size_hint=(.5, .1),text= 'Log_B(B)=1')
        self.add_widget(fifth)
        first.bind(on_release=FirstLaw.display)

class FirstLaw(FloatLayout):

   def display(self,*args):
        popup = Popup(title='Product Law',
              auto_dismiss=False)
        popup.open()
		


class MyApp(App):
    title= "Log Laws"
    def build(self):
        return Menu()


if __name__ == '__main__':
    MyApp().run()