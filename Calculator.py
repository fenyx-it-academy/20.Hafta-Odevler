from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class MainPage(BoxLayout):
    pass

class CalculatorPage(Screen):
    def btn(self,val):
        self.ids.lbl_display.text += val
    def sonuc(self):
        self.ids.lbl_display.text = str(eval(self.ids.lbl_display.text))
    def sil_bironce(self):
        self.ids.lbl_display.text = self.ids.lbl_display.text[:-1]
    def sil_hepsi(self):
        self.ids.lbl_display.text = ""


class SettingsPage(Screen):
    pass

class CalculatorApp(App):
    def build(self):
        return MainPage()



if __name__ == "__main__":
    CalculatorApp().run()


