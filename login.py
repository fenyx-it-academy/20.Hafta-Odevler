from kivy import Config
Config.set('graphics', 'multisamples', '0')


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
class Program(App):
    def build(self):
        #******page1**************************************
        self.AnaSayfa=PageLayout()
        self.ekran_1=FloatLayout()
        self.box=BoxLayout()

        self.giris=Button(text="Login",size_hint=(.3,.1),pos=(110,250))
        self.cikis=Button(text="Quit",size_hint=(.3,.1),pos=(110,180))

        self.ekran_1.add_widget(self.giris)
        self.ekran_1.add_widget(self.cikis)

        self.box.add_widget(self.ekran_1)
        self.AnaSayfa.add_widget(self.box)

        #******page2 vertical duzen *****************************************

        self.ekran_2=BoxLayout(orientation="vertical",padding = [100,20,300,20],spacing = 10)

        self.bos = Label(text="", size_hint=(1, .7))

        self.user=Label(text="User",size_hint=(1,.3))
        self.user_ekran=TextInput(size_hint=(1,.2))

        self.pasword=Label(text="Pasword",size_hint=(1,.2))
        self.pasword_ekran=TextInput(size_hint=(1,.2))

        self.login=Button(text="Login",size_hint=(1,.3))

        self.bos_2 = Label(text="", size_hint=(1, .7))

        self.ekran_2.add_widget(self.bos)
        self.ekran_2.add_widget(self.user)
        self.ekran_2.add_widget(self.user_ekran)
        self.ekran_2.add_widget(self.pasword)
        self.ekran_2.add_widget(self.pasword_ekran)
        self.ekran_2.add_widget(self.login)
        self.ekran_2.add_widget(self.bos_2)
        self.AnaSayfa.add_widget(self.ekran_2)

#************ II istenilen resim Gridlayout duzen***************************************

        # self.ekran_2 = BoxLayout(orientation = "vertical")
        # self.box_1 = GridLayout(rows=3 , padding = [10, 10, 200, 10], size_hint = (1,0.7), spacing = 5)
        #
        # self.user = Label(text="User" , size_hint = (1,1))
        # self.user_ekran = TextInput()
        #
        # self.pasword = Label(text="Password", size_hint = (1,1))
        # self.pasword_screen = TextInput()
        #
        # self.bos3 = Label(text = "")
        # self.bos4 = Label(text = "")
        # self.bos5 = Label(text = "")
        #
        # self.login = Button(text="Login")
        #
        # self.box_1.add_widget(self.user)
        # self.box_1.add_widget(self.pasword_screen)
        # self.box_1.add_widget(self.pasword)
        # self.box_1.add_widget(self.user_ekran)
        # self.box_1.add_widget(self.bos3)
        # self.box_1.add_widget(self.login)
        # self.ekran_2.add_widget(self.bos4)
        # self.ekran_2.add_widget(self.box_1)
        # self.ekran_2.add_widget(self.bos5)

        # self.AnaSayfa.add_widget(self.ekran_2)

        return self.AnaSayfa


Program().run()
