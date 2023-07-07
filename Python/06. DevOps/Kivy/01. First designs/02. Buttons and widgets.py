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
        # We will be working with grids in grids
        self.cols = 1
        self.row_force_default=True
        self.row_default_height=200
        self.col_force_default=True
        self.col_default_width=400


        # Create a second grid layout
        self.top_grid = GridLayout(
            row_force_default=True, # Defaulting the size of the second grid
            row_default_height=100,
            col_force_default=True,
            col_default_width=200)
        
        self.top_grid.cols = 2

        

        # Add widgets
        self.top_grid.add_widget(Label(text="Name: "))

        """
            ,size_hint_y = None, 
            height=150,
            size_hint_x = None,
            width=400))
            """

        #Add Input Box
        self.name = TextInput(multiline=True)
        #Always add a self.add_widget to add them
        self.top_grid.add_widget(self.name)

        # Widget 2
        self.top_grid.add_widget(Label(text="Favorite Pizza: "))
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        # Widget 3
        self.top_grid.add_widget(Label(text="Favorite Color: "))
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)

        # Add the new top_grid to our app
        self.add_widget(self.top_grid)

        # Create a Submit Button
        self.submit = Button(text="Submit",
            font_size=32,
            size_hint_y = None,  #stop changing the height of the button
            height=50,
            size_hint_x = None,
            width=800
            )
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


if __name__== '__main__':
    MyApp().run()