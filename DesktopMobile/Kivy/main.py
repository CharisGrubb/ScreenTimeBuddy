from ast import main

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ReferenceListProperty, ListProperty, StringProperty
from kivy.vector import Vector
from DesktopMobile import Settings




class SlidingStringSetting(BoxLayout):
    options = ListProperty(['Acknowledge', 'Blocking', 'Notification'])
    current_setting = StringProperty('Acknowledge')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
     
    def on_button_press(self):
        
        current_index = self.options.index(self.current_setting)
        next_index = (current_index + 1) % len(self.options)
        self.current_setting = self.options[next_index]
        # db.update_single_setting(user_id="Buddy", setting_key="alert_notification_preference", setting_value=self.current_setting)

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
