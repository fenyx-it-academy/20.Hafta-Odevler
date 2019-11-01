from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Calculator(App):
    def build(self):
        duzen = BoxLayout(orientation="vertical",padding = [5,5,5,5])

        line1 = BoxLayout(size_hint = (1,0.6), padding = [5,5,5,5], spacing = 5)
        butcalculator = Button(text='Calculator', size_hint = (0.2,1),font_size = 17, bold = True)
        butSetting = Button(text="Setting", size_hint = (0.2,1),font_size = 17, bold = True)
        boslabel = Label(text = "", size_hint = (0.8,1))
        line1.add_widget(butcalculator)
        line1.add_widget(butSetting)
        line1.add_widget(boslabel)
        duzen.add_widget(line1)

        line2 = BoxLayout(size_hint = (1,1), padding = [5,5,5,5])
        ekran = Label(text = "")
        line2.add_widget(ekran)
        duzen.add_widget(line2)

        line3 = BoxLayout(size_hint = (1,1.8), padding = [5,5,5,5], spacing = 2)
        but1 = Button(text = "(", size_hint = (0.25,0.25), font_size = 17, bold = True)
        but2 = Button(text = ")", size_hint = (0.25,0.25), font_size = 17, bold = True)
        but3 = Button(text = "/", size_hint = (0.25,0.25), font_size = 17, bold = True)
        but4 = Button(text = "*", size_hint = (0.25,0.25), font_size = 17, bold = True)
        but5 = Button(text = "-", size_hint = (0.25,0.25), font_size = 17, bold = True)
        but6 = Button(text = "C", size_hint = (0.25,0.25), font_size = 17, bold = True)
        but7 = Button(text = "Del", size_hint = (0.25,0.25), font_size = 17, bold = True)
        line3.add_widget(but1)
        line3.add_widget(but2)
        line3.add_widget(but3)
        line3.add_widget(but4)
        line3.add_widget(but5)
        line3.add_widget(but6)
        line3.add_widget(but7)
        duzen.add_widget(line3)


        line4 = BoxLayout(size_hint = (1,2), padding = [15,5,15,5], spacing = 10)
        line4a = GridLayout(cols=3, size_hint = (1,1), spacing = 3)
        butt1 = Button(text = "1", font_size = 20)
        butt2 = Button(text = "2", font_size = 20)
        butt3 = Button(text = "3", font_size = 20)
        butt4 = Button(text = "4", font_size = 20)
        butt5 = Button(text = "5", font_size = 20)
        butt6 = Button(text = "6", font_size = 20)
        butt7 = Button(text = "7", font_size = 20)
        butt8 = Button(text = "8", font_size = 20)
        butt9 = Button(text = "9", font_size = 20)
        butt10 = Button(text = "+", font_size = 20, bold = True, size_hint = (0.2,1))
        line4a.add_widget(butt7)
        line4a.add_widget(butt8)
        line4a.add_widget(butt9)
        line4a.add_widget(butt4)
        line4a.add_widget(butt5)
        line4a.add_widget(butt6)
        line4a.add_widget(butt1)
        line4a.add_widget(butt2)
        line4a.add_widget(butt3)
        line4.add_widget(line4a)
        line4.add_widget(butt10)
        duzen.add_widget(line4)

        line5 = BoxLayout(padding = [5,5,5,5], spacing = 2)
        but0 = Button(text = "0", font_size = 20)
        butnokta = Button(text = ".", font_size = 30, bold = True)
        butesit = Button(text = "=", background_color = [2,0,0,10], font_size = 50, bold = True)
        line5.add_widget(but0)
        line5.add_widget(butnokta)
        line5.add_widget(butesit)
        duzen.add_widget(line5)

        return duzen

Calculator().run()