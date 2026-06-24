from ast import main
from kivy.app import App
from kivy.graphics import Color, Rectangle #Used for overall BG color
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.properties import NumericProperty, ReferenceListProperty, ListProperty, StringProperty
from kivy.vector import Vector
from DesktopMobile import Settings


# #733E24=Brown, #245F73=Blue, #BBBDBC = Gray, #F2F0EF = OffWhite/Light Gray

class SlidingStringSetting(BoxLayout):
    options = ListProperty(['Acknowledge', 'Blocking', 'Notification'])
    current_setting = StringProperty('Acknowledge')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(rgba=get_color_from_hex("#733E24"))
            self.rect = Rectangle(pos=self.pos, size=self.size)
        # Bind size and position changes to update the rectangle
        self.bind(pos=self.update_rect, size=self.update_rect)
    
    def update_rect(self, instance, value):
            self.rect.pos = instance.pos
            self.rect.size = instance.size
   
    def on_button_press(self):
        
        current_index = self.options.index(self.current_setting)
        next_index = (current_index + 1) % len(self.options)
        self.current_setting = self.options[next_index]
        # db.update_single_setting(user_id="Buddy", setting_key="alert_notification_preference", setting_value=self.current_setting)

class Title(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(rgba=get_color_from_hex("#245F73"))
            self.rect = Rectangle(pos=self.pos, size=self.size)
        # Bind size and position changes to update the rectangle
        self.bind(pos=self.update_rect, size=self.update_rect)
    
    def update_rect(self, instance, value):
            self.rect.pos = instance.pos
            self.rect.size = instance.size
        
       

class ScreenTimeBuddyApp(App):
    def build(self):
        self.parent = BoxLayout(orientation='vertical')
        self.parent.add_widget(Title())
        self.parent.add_widget(SlidingStringSetting()) 
        
        return self.parent
    

if __name__ == '__main__':
    ScreenTimeBuddyApp().run()
