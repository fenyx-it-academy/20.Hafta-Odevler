from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout

class Calculator(App):
    def build(self):

        self.anaTablo=FloatLayout()
        self.tuslar=GridLayout(rows=4)
        self.tusTakımı=BoxLayout(size_hint=(.98,.3),pos_hint={'x':.01,'y':.1},orientation='horizontal')

        self.sembol=GridLayout(rows=1,size_hint=(.98,.07), pos_hint={'x':.01, 'y':.41})
        self.altTuslar=BoxLayout(size_hint=(.98,.09),pos_hint={'x':.01, 'y':.01},orientation='horizontal')

        self.arti = Button(text='+',size_hint=(.09,1),font_size=30,color=(.6,.8,.8,2))

        self.calculator=Button(text='Calculator',size_hint=(.2,.05), pos_hint={'x':0, 'top':1})
        self.settings=Button(text='Settings',size_hint=(.2,.05), pos_hint={'x':.2, 'top':1})


        self.solP=Button(text='(',font_size=20,color=(.6,.8,.8,2))
        self.sagP = Button(text=')',font_size=20,color=(.6,.8,.8,2))
        self.Bol = Button(text='/',font_size=20,color=(.6,.8,.8,2))
        self.Cikar = Button(text='--',font_size=30,color=(.6,.8,.8,2))
        self.Carp = Button(text='*',font_size=30,color=(.6,.8,.8,2))
        self.C=Button(text='C',font_size=30,color=(.6,.8,.8,2))
        self.Del=Button(text='Del',font_size=30,color=(.1,.5,2,2))
        for i in [self.solP,self.sagP,self.Bol,self.Cikar,self.Carp,self.C,self.Del]:
            self.sembol.add_widget(i)

        self.bir=Button(text='1',font_size=30)
        self.iki=Button(text='2',font_size=30)
        self.uc = Button(text='3',font_size=30)
        self.dort = Button(text='4',font_size=30)
        self.bes = Button(text='5',font_size=30)
        self.altı = Button(text='6',font_size=30)
        self.yedi = Button(text='7',font_size=30)
        self.sekiz = Button(text='8',font_size=30)
        self.dokuz = Button(text='9',font_size=30)

        for i in [self.bir,self.iki,self.uc,self.dort,self.bes,self.altı,self.yedi,self.sekiz,self.dokuz]:
            self.tuslar.add_widget(i)

        self.sıfır = Button(text='0',size_hint=(.79,1),font_size=30)
        self.nokta = Button(text='.',size_hint=(.79,1),font_size=50,color=(.6,.8,.8,2))
        self.esit = Button(text='=',color=(.6,.8,.8,2),font_size=60,background_color = (2,0,0,2))
        self.altTuslar.add_widget(self.nokta)
        self.altTuslar.add_widget(self.sıfır)
        self.altTuslar.add_widget(self.esit)

        self.tusTakımı.add_widget(self.tuslar)
        self.tusTakımı.add_widget(self.arti)

        # self.ustkose.add_widget(self.calculator)
        # self.ustkose.add_widget(self.settings)

        # self.anaTablo.add_widget(self.ustkose)

        self.anaTablo.add_widget(self.tusTakımı)
        self.anaTablo.add_widget(self.sembol)
        self.anaTablo.add_widget(self.altTuslar)
        self.anaTablo.add_widget(self.calculator)
        self.anaTablo.add_widget(self.settings)



        #
        return self.anaTablo

Calculator().run()
