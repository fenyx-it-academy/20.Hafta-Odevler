from kivy import Config
Config.set('graphics', 'multisamples', '0')


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.actionbar import *


class Program(App):
    def build(self):
        #****ANA PENCERE****************************8
        self.Main_windows=BoxLayout(orientation="vertical")
        #****EN UST ACTION (CALCULATOR,SETTING AYARLARI)***********
        self.Box_1=BoxLayout(orientation="vertical",size_hint=(1,.25))

        self.etiket=ActionBar(size_hint=(1,1))
        self.etiket_viev=ActionView(action_previous=ActionPrevious(with_previous=False))
        self.etiket.add_widget(self.etiket_viev)
        self.etiket_viev.add_widget(ActionButton(text="Calculator"))
        self.etiket_viev.add_widget(ActionButton(text="settings"))

        self.Box_1.add_widget(self.etiket)

        self.Main_windows.add_widget(self.Box_1)

        #******LABEL BOLUMU******************************************8

        self.Box_2=BoxLayout(orientation="vertical")






        self.ekran=Label()
        self.Box_2.add_widget(self.ekran)

        self.Main_windows.add_widget(self.Box_2)
        #******ARITMETIK ISLEMLER BOLUMU***********************************
        self.Box_3=BoxLayout(orientation="vertical",spacing=10,padding=10,size_hint=(1,.3))
        self.box_3_grid=GridLayout(cols=7)

        self.but_1=Button(text="(")
        self.but_2 = Button(text=")")
        self.but_3 = Button(text="/")
        self.but_4 = Button(text="*")
        self.but_5 = Button(text="-")
        self.but_6 = Button(text="C")
        self.but_7 = Button(text="Del")

        self.box_3_grid.add_widget(self.but_1)
        self.box_3_grid.add_widget(self.but_2)
        self.box_3_grid.add_widget(self.but_3)
        self.box_3_grid.add_widget(self.but_4)
        self.box_3_grid.add_widget(self.but_5)
        self.box_3_grid.add_widget(self.but_6)
        self.box_3_grid.add_widget(self.but_7)
        self.Box_3.add_widget(self.box_3_grid)

        self.Main_windows.add_widget(self.Box_3)

        #*******SAYILAR BOLUMU*********************************************
        self.Box_4=BoxLayout(orientetion="horizontal",spacing=10,padding=10)
        self.box_4_grid=GridLayout(cols=3)

        self.sayi_1=Button(text="1")
        self.sayi_2 = Button(text="2")
        self.sayi_3 = Button(text="3")
        self.sayi_4 = Button(text="4")
        self.sayi_5 = Button(text="5")
        self.sayi_6 = Button(text="6")
        self.sayi_7 = Button(text="7")
        self.sayi_8 = Button(text="8")
        self.sayi_9 = Button(text="9")
        self.sayi_arti = Button(text="+",size_hint=(.2,1))

        self.box_4_grid.add_widget(self.sayi_7)
        self.box_4_grid.add_widget(self.sayi_8)
        self.box_4_grid.add_widget(self.sayi_9)
        self.box_4_grid.add_widget(self.sayi_4)
        self.box_4_grid.add_widget(self.sayi_5)
        self.box_4_grid.add_widget(self.sayi_6)
        self.box_4_grid.add_widget(self.sayi_1)
        self.box_4_grid.add_widget(self.sayi_2)
        self.box_4_grid.add_widget(self.sayi_3)

        self.Box_4.add_widget(self.box_4_grid)
        self.Box_4.add_widget(self.sayi_arti)

        self.Main_windows.add_widget(self.Box_4)

        #****EN ALT KISIM (0  ,  .  ,  =  )****************************
        self.Box_5=BoxLayout(orientation="vertical",spacing=10,padding=10,size_hint=(1,.4))
        self.box_5_grid = GridLayout(cols=3)

        self.sayi_0 = Button(text="0")
        self.sayi_nokta = Button(text=".")
        self.sayi_esit = Button(text="=",background_color = [2,0,0,10])

        self.box_5_grid.add_widget(self.sayi_0)
        self.box_5_grid.add_widget(self.sayi_nokta)
        self.box_5_grid.add_widget(self.sayi_esit)

        self.Box_5.add_widget(self.box_5_grid)

        self.Main_windows.add_widget(self.Box_5)

     return self.Main_windows



Program().run()
