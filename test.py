from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.anchorlayout import AnchorLayout


class MyApp(App):
    def build(self):
        bl = AnchorLayout(anchor_x = 'left', anchor_y= 'center')
        bl.add_widget(Button(text = 'Button 1', size_hint = [.5, .5]))
        
        return bl
        

if __name__ == '__main__':
    MyApp().run()