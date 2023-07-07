import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

# VS Code will not recognize it, but it will run
from kivy.properties import ObjectProperty

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



class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__== '__main__':
    MyApp().run()