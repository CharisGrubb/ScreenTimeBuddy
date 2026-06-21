from ast import main

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ReferenceListProperty, ListProperty, StringProperty
from kivy.vector import Vector



class SlidingStringSetting(BoxLayout):
    options = ListProperty(['Acknowledge', 'Blocking', 'Notification'])
    current_setting = StringProperty('Acknowledge')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
     
    def on_slider_value(self, instance, value):
        # Convert the slider's float/int value to index into the string list
        index = int(value)
        self.current_setting = self.options[index]

class Title(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
       

class ScreenTimeBuddyApp(App):
    def build(self):
        parent = BoxLayout(orientation='vertical')
        parent.add_widget(Title())
        parent.add_widget(SlidingStringSetting()) 

        return parent
    

if __name__ == '__main__':
    ScreenTimeBuddyApp().run()
