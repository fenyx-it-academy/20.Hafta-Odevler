print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class Application(App):
    def build(self):
        self.window = FloatLayout()                                        # Hepsinin birarada oldugu buyuk pencere

        self.login = BoxLayout()                                           # herbir pencere icin boxlayout yapildi
        self.quit = BoxLayout()

        self.loginbox = Button(text="Log In", size_hint=(.3, .1), pos_hint={'x': .3, 'y': .62})      # box boyut duzenleme
        self.quitbox = Button(text="Quit", size_hint=(.3, .1), pos_hint={'x': .3, 'y': .5})

        self.window.add_widget(self.loginbox)                              # sirayla penceredeki konumunu cagiriyoruz
        self.window.add_widget(self.quitbox)

        return self.window


if __name__ == "__main__":
    Application().run()


