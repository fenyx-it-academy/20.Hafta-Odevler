from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Klavye(App):
    def build(self):
        duzen = BoxLayout(orientation="vertical", padding = [10,10,10,10])

        line1 = BoxLayout(size_hint = (1,1.3))
        label1 = Label(text="")
        line1.add_widget(label1)
        duzen.add_widget(line1)

        line2 = BoxLayout(size_hint = (1,0.15))
        yazialani = TextInput()
        line2.add_widget(yazialani)
        duzen.add_widget(line2)

        line3 = BoxLayout(orientation = "vertical", padding = [20,10,20,10])
        line3a = BoxLayout(spacing = 1, padding = [0,0,0,2])
        line3a.add_widget(Button(text = "`", size_hint = (0.8,1)))
        line3a.add_widget(Button(text = "1", size_hint = (0.8,1)))
        line3a.add_widget(Button(text = "2", size_hint = (0.8,1)))
        line3a.add_widget(Button(text = "3", size_hint = (0.8,1)))
        line3a.add_widget(Button(text = "4", size_hint = (0.8,1)))
        line3a.add_widget(Button(text = "5", size_hint = (0.8,1)))
        line3a.add_widget(Button(text = "6", size_hint = (0.8,1)))
        line3a.add_widget(Button(text = "7", size_hint = (0.8,1)))
        line3a.add_widget(Button(text = "8", size_hint = (0.8,1)))
        line3a.add_widget(Button(text = "9", size_hint = (0.8,1)))
        line3a.add_widget(Button(text = "0", size_hint = (0.8,1)))
        line3a.add_widget(Button(text = "-", size_hint = (0.8,1)))
        line3a.add_widget(Button(text = "=", size_hint = (0.8,1)))
        line3a.add_widget(Button(text = "Backspace", size_hint = (1.4,1)))
        line3.add_widget(line3a)

        line3b = BoxLayout(padding = [0,0,20,2], spacing = 1)
        line3b.add_widget(Button(text="Tab", size_hint = (1.2,1)))
        line3b.add_widget(Button(text="q", size_hint = (0.8,1)))
        line3b.add_widget(Button(text="w", size_hint = (0.8,1)))
        line3b.add_widget(Button(text="e", size_hint = (0.8,1)))
        line3b.add_widget(Button(text="r", size_hint = (0.8,1)))
        line3b.add_widget(Button(text="t", size_hint = (0.8,1)))
        line3b.add_widget(Button(text="y", size_hint = (0.8,1)))
        line3b.add_widget(Button(text="u", size_hint = (0.8,1)))
        line3b.add_widget(Button(text="i", size_hint = (0.8,1)))
        line3b.add_widget(Button(text="o", size_hint = (0.8,1)))
        line3b.add_widget(Button(text="p", size_hint = (0.8,1)))
        line3b.add_widget(Button(text="[", size_hint = (0.8,1)))
        line3b.add_widget(Button(text="]", size_hint = (0.8,1)))
        line3b.add_widget(Button(text="'\\", size_hint = (0.8,1)))
        line3.add_widget(line3b)

        line3c = BoxLayout(spacing = 1, padding = [0,0,0,2])
        line3c.add_widget(Button(text="CapsLock",size_hint = (1.4,1)))
        line3c.add_widget(Button(text="a", size_hint = (0.8,1)))
        line3c.add_widget(Button(text="s", size_hint = (0.8,1)))
        line3c.add_widget(Button(text="d", size_hint = (0.8,1)))
        line3c.add_widget(Button(text="f", size_hint = (0.8,1)))
        line3c.add_widget(Button(text="g", size_hint = (0.8,1)))
        line3c.add_widget(Button(text="h", size_hint = (0.8,1)))
        line3c.add_widget(Button(text="j", size_hint = (0.8,1)))
        line3c.add_widget(Button(text="k", size_hint = (0.8,1)))
        line3c.add_widget(Button(text="l", size_hint = (0.8,1)))
        line3c.add_widget(Button(text=";", size_hint = (0.8,1)))
        line3c.add_widget(Button(text="'", size_hint = (0.8,1)))
        line3c.add_widget(Button(text="Enter",size_hint = (1.4,1)))
        line3.add_widget(line3c)

        line3d = BoxLayout(spacing = 1, padding = [0,0,0,2])
        line3d.add_widget(Button(text="Shift", size_hint = (1.7,1)))
        line3d.add_widget(Button(text="z", size_hint = (0.8,1)))
        line3d.add_widget(Button(text="x", size_hint = (0.8,1)))
        line3d.add_widget(Button(text="c", size_hint = (0.8,1)))
        line3d.add_widget(Button(text="v", size_hint = (0.8,1)))
        line3d.add_widget(Button(text="b", size_hint = (0.8,1)))
        line3d.add_widget(Button(text="n", size_hint = (0.8,1)))
        line3d.add_widget(Button(text="m", size_hint = (0.8,1)))
        line3d.add_widget(Button(text=",", size_hint = (0.8,1)))
        line3d.add_widget(Button(text=".", size_hint = (0.8,1)))
        line3d.add_widget(Button(text="/", size_hint = (0.8,1)))
        line3d.add_widget(Button(text="Shift", size_hint = (1.7,1)))
        line3.add_widget(line3d)

        line3e = BoxLayout(spacing = 1, padding = [0,0,0,2])
        line3e.add_widget(Button(text="Ctrl", size_hint = (0.7,1)))
        line3e.add_widget(Button(text="Fn", size_hint = (0.7,1)))
        line3e.add_widget(Button(text="Wnds", size_hint = (0.7,1)))
        line3e.add_widget(Button(text="Alt", size_hint = (0.7,1)))
        line3e.add_widget(Button(text="", size_hint = (4,1)))
        line3e.add_widget(Button(text="Alt gr", size_hint = (1.2,1)))
        line3e.add_widget(Button(text="Ctrl", size_hint = (1.2,1)))
        line3e.add_widget(Button(text="X", size_hint = (1.2,1)))
        line3.add_widget(line3e)
        duzen.add_widget(line3)



        return duzen


Klavye().run()
