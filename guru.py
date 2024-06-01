from kivy.uix.actionbar import BoxLayout
from kivy.app import App
from kivy.uix.screenmanager import Screen , ScreenManager
from kivy.uix.widget import Widget
from kivy.lang import Builder


# from kivy.core.window import Window

Builder.load_file ('my.kv')


# Window.clearcolor =(41, 97, 166)
class Homepage(Screen):
    pass
class Mylayout(Widget):
    pass
class JapjiSahib(Screen):
    pass


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Homepage(name='home'))
        sm.add_widget(JapjiSahib(name='japji'))
        # sm.add_widget(Mylayout(name='mylayout'))
        # Builder.load_string(kv)
        

        return sm

if __name__=="__main__":
    MyApp().run()
# this is a kv. file code 
