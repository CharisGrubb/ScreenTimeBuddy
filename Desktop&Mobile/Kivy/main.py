from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class MainWidget(Widget):
    pass


class ScreenTimeBuddyApp(App):
    def build(self):
        return MainWidget()
    

if __name__ == '__main__':
    ScreenTimeBuddyApp().run()
