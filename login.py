from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class Programx(App):
    def build(self):

        self.mainFrame = FloatLayout() # Elemanların hepsini tutan ana pencere düzenimiz

        self.login = BoxLayout()
        self.quit = BoxLayout()

        self.login_buton = Button(background_color=(.6, .4, .8, 1), text ="Login",
                                  size_hint=(.2, .1), pos_hint={'x': .2, 'y': .44})
        self.quit_buton = Button(background_color=(.6, .4, .8, 1), text="Quit",
                                 size_hint=(.2, .1), pos_hint={'x': .2, 'y': .56})


        # Şimdi hepsini ana düzene yerleştiriyoruz

        self.mainFrame.add_widget(self.login)
        self.mainFrame.add_widget(self.quit)
        self.mainFrame.add_widget(self.login_buton)
        self.mainFrame.add_widget(self.quit_buton)

        return self.mainFrame

Programx().run()