import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# VS Code will not recognize it, but it will run
from kivy.properties import ObjectProperty

# Import deisgn file
Builder.load_file("design_file.kv")

class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    # Define function press to determine what happenes when the user presses the button
    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        

        print(f'Hello {name}. you like {pizza} pizza, and your favorite color is {color}!')

        # Clear the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


""" You can import the deisgn file as a class
# Example: elder.kv, then class Elder(App):
# If design file is name my.kv, then MyApp works
class MyApp(App): 
    def build(self):
        return MyGridLayout()
"""

class AwsomeApp(App): 
    def build(self):
        return MyGridLayout()

if __name__== '__main__':
    AwsomeApp().run()