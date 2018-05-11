from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.properties import ObjectProperty, NumericProperty

import Menu

sm = None

class FirstLaw(Screen):
    def __init__(self, **kwargs):
        super(FirstLaw, self).__init__(**kwargs)
        self.Display()
        self.OnClick()

    def Display(self):
        variable1=Label(text='let Log(M)= ',pos=(-325,220))
        variable1.font_size = '20dp'
        self.add_widget(variable1)
        self.v1 = TextInput(text='',pos_hint={'x': .2, 'center_y': .9}, size_hint=(.1, .1))
        self.add_widget(self.v1)
        variable2=Label(text='let Log(N)= ',pos=(-100,220))
        variable2.font_size = '20dp'
        self.add_widget(variable2)
        self.v2 = TextInput(text='',pos_hint={'x': .45, 'center_y': .9}, size_hint=(.1, .1))
        self.add_widget(self.v2)
        self.submit = Button(pos_hint={'x': .25, 'center_y': .8}, size_hint=(.1, .05),text= 'Enter')
        self.add_widget(self.submit) 
        self.back = Button(pos_hint={'x': .05, 'center_y': .05}, size_hint=(.1, .05),text= 'Back')
        self.add_widget(self.back) 
    
    def OnClick(self):
        self.submit.bind(on_release=self.Proof)
        self.back.bind(on_release=self.Switch_menu)
    
    def Switch_menu(self,*args):
        global sm
        sm.add_widget(Menu.Menu(name="Menu"))
        sm.current = "Menu"
        Menu.sm = sm
        return 

    def Proof(self,*args):
        pass
        #X=self.v1.text
      #  X='x'
    

