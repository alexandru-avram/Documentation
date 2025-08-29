import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


# VS Code will not recognize it, but it will run
from kivy.properties import ObjectProperty

# Import deisgn file
Builder.load_file("float_layout.kv")

class MyLayout(Widget):
    pass


class AwsomeApp(App): 
    def build(self):
        return MyLayout()


if __name__== '__main__':
    AwsomeApp().run()