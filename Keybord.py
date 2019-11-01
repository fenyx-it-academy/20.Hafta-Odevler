#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout

class Keybord(App):
    def build(self):

        self.anaEkran=FloatLayout()

        self.ilkSatır=BoxLayout(size_hint=(.9,.07),pos_hint={'x':.05,'y':.3},orientation='horizontal')
#background_normal=('kivy.png')
        self.tirnak=Button(text='é',font_size=20,size_hint=(.5,1))
        self.bir = Button(text='1', font_size=20,size_hint=(.5,1))
        self.iki = Button(text='2', font_size=20,size_hint=(.5,1))
        self.uc = Button(text='3', font_size=20,size_hint=(.5,1))
        self.dort = Button(text='4', font_size=20,size_hint=(.5,1))
        self.bes = Button(text='5', font_size=20,size_hint=(.5,1))
        self.altı = Button(text='6', font_size=20,size_hint=(.5,1))
        self.yedi = Button(text='7', font_size=20,size_hint=(.5,1))
        self.sekiz = Button(text='8', font_size=20,size_hint=(.5,1))
        self.dokuz = Button(text='9', font_size=20,size_hint=(.5,1))
        self.sıfır = Button(text='0', font_size=20,size_hint=(.5,1))
        self.yıldız = Button(text='*', font_size=20,size_hint=(.5,1))
        self.esit = Button(text='=', font_size=20,size_hint=(.5,1))
        self.backSpace=Button(text='Back',font_size=20)

        for i in [self.tirnak,self.bir,self.iki,self.uc,self.dort,self.bes,self.altı,self.yedi,self.sekiz,
                  self.dokuz,self.sıfır,self.yıldız,self.esit,self.backSpace]:
            self.ilkSatır.add_widget(i)

        self.ikinciSatır = BoxLayout(size_hint=(.87,.07),pos_hint={'x':.05,'y':.23},orientation='horizontal')

        self.tab = Button(text='Tab', font_size=20)
        self.bir = Button(text='q', font_size=20, size_hint=(.7, 1))
        self.iki = Button(text='w', font_size=20, size_hint=(.7, 1))
        self.uc = Button(text='e', font_size=20, size_hint=(.7, 1))
        self.dort = Button(text='r', font_size=20, size_hint=(.7, 1))
        self.bes = Button(text='t', font_size=20, size_hint=(.7, 1))
        self.altı = Button(text='y', font_size=20, size_hint=(.7, 1))
        self.yedi = Button(text='u', font_size=20, size_hint=(.7, 1))
        self.sekiz = Button(text='i', font_size=20, size_hint=(.7, 1))
        self.dokuz = Button(text='o', font_size=20, size_hint=(.7, 1))
        self.sıfır = Button(text='p', font_size=20, size_hint=(.7, 1))
        self.yıldız = Button(text='[', font_size=20, size_hint=(.7, 1))
        self.esit = Button(text=']', font_size=20, size_hint=(.7, 1))
        self.backSpace = Button(text='\\', font_size=20,size_hint=(.7, 1))

        for i in [self.tab,self.bir,self.iki,self.uc,self.dort,self.bes,self.altı,self.yedi,self.sekiz,
                  self.dokuz,self.sıfır,self.yıldız,self.esit,self.backSpace]:
            self.ikinciSatır.add_widget(i)

        self.ucuncuSatır = BoxLayout(size_hint=(.9,.07), pos_hint={'x': .05, 'y':.16}, orientation='horizontal')

        self.caps = Button(text='Caps', font_size=20)
        self.a = Button(text='a', font_size=20, size_hint=(.5, 1))
        self.s = Button(text='s', font_size=20, size_hint=(.5, 1))
        self.d = Button(text='d', font_size=20, size_hint=(.5, 1))
        self.f = Button(text='f', font_size=20, size_hint=(.5, 1))
        self.g = Button(text='g', font_size=20, size_hint=(.5, 1))
        self.h = Button(text='h', font_size=20, size_hint=(.5, 1))
        self.j = Button(text='j', font_size=20, size_hint=(.5, 1))
        self.k = Button(text='k', font_size=20, size_hint=(.5, 1))
        self.l = Button(text='l', font_size=20, size_hint=(.5, 1))
        self.ikiNokta = Button(text=':', font_size=20, size_hint=(.5, 1))
        self.backSlach = Button(text='\'', font_size=20, size_hint=(.5, 1))
        self.enter = Button(text='Enter', font_size=20)

        for i in [self.caps, self.a, self.s, self.d, self.f, self.g, self.h, self.j, self.k,
                  self.l, self.ikiNokta, self.backSlach, self.enter]:
            self.ucuncuSatır.add_widget(i)

        self.dorduncuSatır = BoxLayout(size_hint=(.9, .07), pos_hint={'x': .05, 'y': .09}, orientation='horizontal')

        self.shift = Button(text='Shift', font_size=20)
        self.z = Button(text='z', font_size=20, size_hint=(.39, 1))
        self.x = Button(text='x', font_size=20, size_hint=(.39, 1))
        self.c = Button(text='c', font_size=20, size_hint=(.39, 1))
        self.v = Button(text='v', font_size=20, size_hint=(.39, 1))
        self.b = Button(text='b', font_size=20, size_hint=(.39, 1))
        self.n = Button(text='n', font_size=20, size_hint=(.39, 1))
        self.m = Button(text='m', font_size=20, size_hint=(.39, 1))
        self.virgul = Button(text=',', font_size=20, size_hint=(.39, 1))
        self.nokta = Button(text='.', font_size=20, size_hint=(.39, 1))
        self.slach = Button(text='/', font_size=20, size_hint=(.39, 1))
        self.shift2 = Button(text='Shift', font_size=20)
        for i in [self.shift, self.z, self.x, self.c, self.v, self.b, self.n, self.m, self.virgul,
                  self.nokta, self.slach,self.shift2]:
            self.dorduncuSatır.add_widget(i)


        self.besinciSatır = BoxLayout(size_hint=(.9, .07), pos_hint={'x': .05, 'y': .02}, orientation='horizontal')

        self.ctrl = Button(text='Ctrl', font_size=20, size_hint=(.15, 1))
        self.space = Button(text='Space', font_size=20)
        self.win = Button(text='Win', font_size=20, size_hint=(.15, 1))
        self.X = Button(text='X', font_size=20, size_hint=(.15, 1))

        for i in [self.ctrl,self.space,self.win,self.X]:
            self.besinciSatır.add_widget(i)


        self.anaEkran.add_widget(TextInput(size_hint=(.9, .58), pos_hint={'x': .05, 'y': .4}))
        self.anaEkran.add_widget(self.ilkSatır)
        self.anaEkran.add_widget(self.ikinciSatır)
        self.anaEkran.add_widget(self.ucuncuSatır)
        self.anaEkran.add_widget(self.dorduncuSatır)
        self.anaEkran.add_widget(self.besinciSatır)
        return self.anaEkran

Keybord().run()