print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


Builder.load_file("calculator.kv")
Window.clearcolor = .2, .3, .3, 1


class Calculate(Screen):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"


class Properties(Screen):
    pass


class Setting(Screen):
    pass


class Window(ScreenManager):
    pass


class calc(App):
    def build(self):
        self.title = "Calculator"
        return Window()


if __name__ == '__main__':
    calc().run()
