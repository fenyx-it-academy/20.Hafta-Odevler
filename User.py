from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class User(App):
    def build(self):
        self.anaPencere=BoxLayout(size_hint=(.4,.2),pos_hint= {'x': .3,'y':.4},orientation='vertical',)


        self.ilksatır=BoxLayout()
        self.ikincisatır=BoxLayout()

        self.kullanıcı=Label(text='User:')
        self.kullanıcıKutu=TextInput()

        self.sifre=Label(text='Password:')
        self.siferKutu=TextInput()

        self.buton=Button(size_hint=(.5,1),pos_hint={'x':.5,'y':0},text='Log in')

        self.ilksatır.add_widget(self.kullanıcı)
        self.ilksatır.add_widget(self.kullanıcıKutu)

        self.ikincisatır.add_widget(self.sifre)
        self.ikincisatır.add_widget(self.siferKutu)

        self.anaPencere.add_widget(self.ilksatır)
        self.anaPencere.add_widget(self.ikincisatır)
        self.anaPencere.add_widget(self.buton)

        return self.anaPencere

User().run()