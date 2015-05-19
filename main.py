#!/usr/bin/python

import kivy

#kivy.require('1.0.6') # replace with your current kivy version !
__version__ = '0.0.1'

from kivy.app import App
from kivy.uix.button import Button

#from plyer.notification import notify


class MyApp(App):
    def build(self):
        return Button(text='Hello World')

if __name__ == '__main__':
    MyApp().run()
