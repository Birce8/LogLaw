from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, NumericProperty

class FirstLaw(Screen):

    def __init__(self, **kwargs):
        super(FirstLaw, self).__init__(**kwargs)
        variable1=Label(text='let Log(M)= ',pos=(-325,220))
        variable1.font_size = '20dp'
        self.add_widget(variable1)
        self.v1 = TextInput(text='',pos_hint={'x': .2, 'center_y': .9}, size_hint=(.1, .1))
        self.add_widget(self.v1)
        variable2=Label(text='let Log(N)= ',pos=(-100,220))
        variable2.font_size = '20dp'
        self.add_widget(variable2)
