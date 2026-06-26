from ast import main
from kivy.app import App
from kivy.graphics import Color, Rectangle #Used for overall BG color
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.properties import NumericProperty, ReferenceListProperty, ListProperty, StringProperty
from DesktopMobile import Settings


# #733E24=Brown, #245F73=Blue, #BBBDBC = Gray, #F2F0EF = OffWhite/Light Gray
class TimeSpinner(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(rgba=get_color_from_hex("#733E24"))
            self.rect = Rectangle(pos=self.pos, size=self.size)
        # Bind size and position changes to update the rectangle
        self.bind(pos=self.update_rect, size=self.update_rect)
       
        
        self.box = BoxLayout(orientation='horizontal'
                             ,spacing=10
                             ,size_hint=(None,None)
                             ,pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # Bind the minimum size of children to the box size
        self.box.bind(minimum_size = self.box.setter('size'))
     
        self.label = Label(text = "Alerting Time Interval:"
                           , height = 44
                           , size_hint = (None,None))
        self.label.bind(texture_size=self.label.setter('size')) # Shrink bounds to text size
        self.box.add_widget(self.label)

        self.hour_spinner =  Spinner(
            text='12',
            values=('12', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11'),
            size_hint=(None, None),
            size=(100, 44),)
        
        self.minute_spinner=  Spinner(
            text='00',
            values=('00', '15', '30', '45'),
            size_hint=(None, None),
            size=(100, 44))
        
        self.box.add_widget(self.hour_spinner)
        self.box.add_widget(self.minute_spinner)

        self.add_widget(self.box)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

   
         
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
        #db.update_single_setting(user_id="Buddy", setting_key="alert_notification_preference", setting_value=self.current_setting)

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
      
        self.parent.add_widget(TimeSpinner())
        self.parent.add_widget(SlidingStringSetting()) 
        
        return self.parent
    

if __name__ == '__main__':
    ScreenTimeBuddyApp().run()
