import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
#from kivy.core.window import Window

# VS Code will not recognize it, but it will run
from kivy.properties import ObjectProperty

# Import deisgn file
Builder.load_file("inherit.kv")

class MyLayout(Widget):
    pass


class AwsomeApp(App): 
    def build(self):
        #Window.clearcolor = (1,1,1,1)
        return MyLayout()


if __name__== '__main__':
    AwsomeApp().run()