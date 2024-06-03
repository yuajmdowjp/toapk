from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


class Interface(BoxLayout):
    num_text=StringProperty(' ')
    num=' '
    b=False
    def button_click(self,n):
        if self.b:
            self.num=' '
            self.b=False
        if n=='C':
            self.num=' '
            self.b=False
        elif n=='=':
            self.b=True
            self.num=str(eval(self.num))
        else:
            self.num+=n
        self.num_text=self.num



class CalculatorApp(App):
    def build(self):
        Window.size=(500,650)

CalculatorApp().run()