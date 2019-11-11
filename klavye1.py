from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class MyKeybordDesign(BoxLayout):
    lbl_display  = ObjectProperty(None)
    txt_inp_display = ObjectProperty(None)
    btn_dalga = ObjectProperty(None)
    btn_1 = ObjectProperty(None)

    def btn(self,val):
        # self.ids.txt_inp_display.text += self.ids.btn_dalga.text
        # self.ids.lbl_display.text =self.ids.btn_dalga.text
        self.ids.txt_inp_display.text += val


kv = Builder.load_file("klavye1.kv")

class MyKeybord(App):
    def build(self):
        return MyKeybordDesign()

if __name__ == "__main__":
    MyKeybord().run()