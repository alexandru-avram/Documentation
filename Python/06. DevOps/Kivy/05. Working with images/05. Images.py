import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window

# Import deisgn file
Builder.load_file("design_images.kv")

class MyLayout(Widget):
    pass


class AwsomeApp(App): 
    def build(self):
        Window.clearcolor = (0,0,0,1)
        return MyLayout()


if __name__== '__main__':
    AwsomeApp().run()