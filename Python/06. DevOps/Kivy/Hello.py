import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set number of columns
        # Kivy will determine how to arrange them
        self.cols = 2

        # Add widgets
        self.add_widget(Label(text="Name: "))

        #Add Input Box
        self.name = TextInput(multiline=False)
        #Always add a self.add_widget to add them
        self.add_widget(self.name)

        # Widget 2
        self.add_widget(Label(text="Favorite Pizza: "))
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        # Widget 3
        self.add_widget(Label(text="Favorite Color: "))
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

        # Create a Submit Button
        self.submit = Button(text="Submit",font_size=32)
        #Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    # Define function press to determine what happenes when the user presses the button
    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        
        # Print it in the terminal
        # print(f'Hello {name}. you like {pizza} pizza, and your favorite color is {color}!')

        self.add_widget(Label(text=f'Hello {name}. you like {pizza} pizza, and your favorite color is {color}!'))

        # Clear the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()


"""
Simple class used to create a text with "Hello World"

class MyApp(App):
    def build(self):
        return Label (text="Hello World", font_size=72)
"""    

if __name__== '__main__':
    MyApp().run()