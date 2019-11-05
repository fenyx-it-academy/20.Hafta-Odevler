print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class secreen(App):
    def build(self):
        self.window = BoxLayout(orientation="vertical",
                                   size_hint=(.5, .25),
                                   pos_hint={'x': .15, 'y': .4})                # Hepsinin birarada oldugu buyuk pencere

        self.username = BoxLayout()                                             # herbir pencere icin boxlayout yapildi
        self.password = BoxLayout()
        self.login = BoxLayout()

        self.usernameLabel = Label(text="Username", size_hint=(.3, .2))                         # username label duzenleme
        self.usernamebox = TextInput(size_hint=(.4, .95))                                       # box boyut duzenleme
        self.passwordLabel = Label(text="Password", size_hint=(.3, .2))                         # password etiket duzenleme
        self.passwordbox = TextInput(size_hint=(.4, .95), password=True, password_mask="*")     # password box duzenleme
        self.loginLabel = Label(size_hint=(.3, .1))                                             # login etiket duzenleme
        self.loginbuton = Button(background_color=(.16, .14, .8, 1), text="Login", size_hint=(.4, .9))   # login box duzenleme

        self.username.add_widget(self.usernameLabel)                                          # herbirine widget ekleme
        self.username.add_widget(self.usernamebox)
        self.password.add_widget(self.passwordLabel)
        self.password.add_widget(self.passwordbox)
        self.login.add_widget(self.loginLabel)
        self.login.add_widget(self.loginbuton)

        # Enson sirayla pencereye yerlestirme

        self.window.add_widget(self.username)
        self.window.add_widget(self.password)
        self.window.add_widget(self.login)

        return self.window


if __name__ == '__main__':
    secreen().run()
