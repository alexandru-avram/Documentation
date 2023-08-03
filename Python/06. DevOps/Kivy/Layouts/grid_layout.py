import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# VS Code will not recognize it, but it will run
from kivy.properties import ObjectProperty

# Import deisgn file
Builder.load_file("grid_layout.kv")

class MyGridLayout(Widget):

    name1 = ObjectProperty(None)
    name2 = ObjectProperty(None)
    name3 = ObjectProperty(None)

    # Define function press to determine what happenes when the user presses the button
    def press(self):
        name1 = self.name1.text
        name2 = self.name2.text
        name3 = self.name3.text
        

        print(f'{name1}. {name2} {name3} will be printed on the console')

        # Clear the input boxes
        self.name1.text = ""
        self.name2.text = ""
        self.name3.text = ""

class AwsomeApp(App): 
    def build(self):
        return MyGridLayout()

if __name__== '__main__':
    AwsomeApp().run()