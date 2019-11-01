from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class Pencere(App):
    def build(self):
        duzen = PageLayout()
        page1 = BoxLayout(orientation = "vertical")
        page1a = BoxLayout(orientation = "vertical", padding = [100,10,500,10], size_hint = (1,0.5), spacing = 5)
        buton1 = Button(text="Log In")
        buton2 = Button(text='Quit')
        label1 = Label(text="")
        label2 = Label(text="")
        page1a.add_widget(buton1)
        page1a.add_widget(buton2)
        page1.add_widget(label1)
        page1.add_widget(page1a)
        page1.add_widget(label2)
        duzen.add_widget(page1)

        page2 = BoxLayout(orientation = "vertical")
        page2a = GridLayout(rows=3 , padding = [10, 10, 200, 10], size_hint = (1,0.7), spacing = 5)
        but1 = Button(text="Log In")
        lab1 = Label(text="User" , size_hint = (1,1))
        lab2 = Label(text="Password", size_hint = (1,1))
        lab3 = Label(text = "")
        lab4 = Label(text = "")
        lab5 = Label(text = "")
        tex1 = TextInput()
        tex2 = TextInput()
        page2a.add_widget(lab1)
        page2a.add_widget(tex2)
        page2a.add_widget(lab2)
        page2a.add_widget(tex1)
        page2a.add_widget(lab3)
        page2a.add_widget(but1)
        page2.add_widget(lab4)
        page2.add_widget(page2a)
        page2.add_widget(lab5)

        duzen.add_widget(page2)

        return duzen
Pencere().run()

