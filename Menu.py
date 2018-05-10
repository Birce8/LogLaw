from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, NumericProperty

import FirstLaw

sm = None

class Menu(Screen):
    BUTTON_SIZE = (.5, .1)
    __first = None
    __second = None
    __third = None
    __forth = None
    __fifth = None
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.initScreenProperties()
        self.initWidgets()
        self.initOnClicks()
    def initScreenProperties(self):
        self.cols = 2
        title=Label(text='Logarithmic Laws',pos=(-125,220))
        title.font_size = '40dp'
        self.add_widget(title)
    def initWidgets(self):
        self.__first = Button(pos_hint={'x': .1, 'center_y': .7}, size_hint=self.BUTTON_SIZE,text= 'Log_B(MN)=Log_B(M)+Log_B(N)')
        self.add_widget(self.__first)
        self.__second = Button(pos_hint={'x': .1, 'center_y': .6}, size_hint=self.BUTTON_SIZE,text= 'Log_B(M/N)=Log_B(M)-Log_B(N)')
        self.add_widget(self.__second)
        self.__third = Button(pos_hint={'x': .1, 'center_y': .5}, size_hint=self.BUTTON_SIZE,text= 'Log_B(M^R)=RLog_B(M)')
        self.add_widget(self.__third)
        self.fourth = Button(pos_hint={'x': .1, 'center_y': .4}, size_hint=self.BUTTON_SIZE,text= 'Log_B(1)=0')
        self.add_widget(self.fourth)
        self.__fifth= Button(pos_hint={'x': .1, 'center_y': .3}, size_hint=self.BUTTON_SIZE,text= 'Log_B(B)=1')
        self.add_widget(self.__fifth)
    def initOnClicks(self):
        self.__first.bind(on_release=self.Switch_First_Law)
    def Switch_First_Law(self, *args):
        sm.add_widget(FirstLaw.FirstLaw(name="FirstLaw"))
        sm.current = "FirstLaw"
        return
