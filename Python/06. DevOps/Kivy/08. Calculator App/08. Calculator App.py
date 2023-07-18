import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window

# Set the app size
Window.size = (500,700)


# Import deisgn file
Builder.load_file("calculator_design.kv")




class MyLayout(Widget):
    pass



class  CalculatorApp(App): 
    def build(self):
        return MyLayout()


if __name__== '__main__':
    CalculatorApp().run()