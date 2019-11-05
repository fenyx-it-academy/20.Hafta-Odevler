print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder


Builder.load_file("keyboard.kv")

class Keyboard(App):
    pass


Keyboard().run()
