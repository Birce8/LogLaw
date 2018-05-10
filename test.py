from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt
import numpy as np
import math

class graph(BoxLayout):
    def __init__(self, **kwargs):
        super(graph, self).__init__(**kwargs)
        x=np.linspace(1,10)
        plt.plot(x, np.log2(x),x,np.log10(x))
        plt.ylabel('some numbers')
        self.add_widget(FigureCanvasKivyAgg(plt.gcf()))


class MyApp(App):

    def build(self):
        
        return graph()

MyApp().run()

# import numpy as np
# import matplotlib.pyplot as plt

# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)

# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)

# plt.figure(1)
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()