from kivy import Config
Config.set('graphics', 'multisamples', '0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout



class Klavye(App):

    def build(self):
        self.Pencere=BoxLayout(orientation="vertical")
        self.bos = BoxLayout(orientation="vertical")
        self.ekran_box =FloatLayout()

        self.ekran = TextInput(size_hint=(1,.2),pos=(100,200))
        self.ekran_box.add_widget(self.ekran)

        self.klavye_box = AnchorLayout(anchor_x="right", anchor_y="bottom")
        self.klavye = VKeyboard()
        self.klavye_box.add_widget(self.klavye)

        self.Pencere.add_widget(self.bos)
        self.Pencere.add_widget(self.ekran_box)
        self.Pencere.add_widget(self.klavye_box)

        return self.Pencere


Klavye().run()

