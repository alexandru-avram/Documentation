import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.core.window import Window

# Set the app size
Window.size = (600,300)



class MyGridLayout(GridLayout):
# Initialize infinite keywords
    def __init__(self, **kwargs):

        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # TOP GRID
        self.cols = 1

        self.add_widget(Label(text="SELECT A LAYOUT", font_size = 32))


        # BOTTOM GRID
        self.bottom_grid = GridLayout(row_force_default=True,
            row_default_height=150,
            col_force_default=True,
            col_default_width=200)
        
        
        self.bottom_grid.cols = 3
        

        self.bottom_grid.add_widget(Button(text="Grid Layout", on_press=self.grid_layout_pressed))
        self.bottom_grid.add_widget(Button(text="Box Layout", on_press=self.box_layout_pressed))
        self.bottom_grid.add_widget(Button(text="Float Layout", on_press=self.float_layout_pressed))
        self.add_widget(self.bottom_grid)

        # Define the functions for each button command

    def grid_layout_pressed(self, instance):
        print("Grid Layout button pressed!")

    def box_layout_pressed(self, instance):
        print("Box Layout button pressed!")


    def float_layout_pressed(self, instance):
        print("Float Layout button pressed!")        
        



class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__== '__main__':
    MyApp().run()