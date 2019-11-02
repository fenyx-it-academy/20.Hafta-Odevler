from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class Programx(App):
    def build(self):

        self.mainFrame = PageLayout()
        self.page1BL = BoxLayout()
        self.page2BL = BoxLayout()

        #################### PAGE 1 ################################
        self.mainFramePG1 = FloatLayout()  # Elemanların hepsini tutan ana pencere düzenimiz

        self.login = BoxLayout()
        self.quit = BoxLayout()

        self.login_buton = Button(background_color=(.6, .4, .8, 1), text="Login",
                                  size_hint=(.2, .1), pos_hint={'x': .2, 'y': .44})
        self.quit_buton = Button(background_color=(.6, .4, .8, 1), text="Quit",
                                 size_hint=(.2, .1), pos_hint={'x': .2, 'y': .56})

        # Şimdi hepsini ana düzene yerleştiriyoruz

        self.mainFramePG1.add_widget(self.login)
        self.mainFramePG1.add_widget(self.quit)
        self.mainFramePG1.add_widget(self.login_buton)
        self.mainFramePG1.add_widget(self.quit_buton)


        ################## PAGE 2 ##############################

        self.mainFramePG2 = BoxLayout(orientation ="vertical",
                                      size_hint=(.5, .25), pos_hint={'x': .15, 'y': .4}) # Elemanların hepsini tutan ana pencere düzenimiz

        self.user = BoxLayout()
        self.password = BoxLayout()
        self.login = BoxLayout()

        self.userLabel = Label(text = "Username", size_hint=(.4, .95))
        self.userInput = TextInput(size_hint=(.6, .95))

        self.user.add_widget(self.userLabel)
        self.user.add_widget(self.userInput)

        self.passwordLabel = Label(text="Password", size_hint=(.4, .95))
        self.passwordInput = TextInput(size_hint=(.6, .95))

        self.password.add_widget(self.passwordLabel)
        self.password.add_widget(self.passwordInput)

        self.loginLabel = Label(size_hint=(.4, .9))
        self.login_buton = Button(background_color=(.6, .4, .8, 1), text = "Login", size_hint=(.6, .9))
        self.login.add_widget(self.loginLabel)
        self.login.add_widget(self.login_buton)



        # Şimdi hepsini ana düzene yerleştiriyoruz

        self.mainFramePG2.add_widget(self.user)
        self.mainFramePG2.add_widget(self.password)
        self.mainFramePG2.add_widget(self.login)

        self.page1BL.add_widget(self.mainFramePG1)
        self.page2BL.add_widget(self.mainFramePG2)
        self.mainFrame.add_widget(self.page1BL)
        self.mainFrame.add_widget(self.page2BL)

        return self.mainFrame

Programx(title = "Login Page").run()