# Kivy 

[Kivy Documentation](https://kivy.org/doc/stable/)

## Begginner Level

### [Hello World](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/01.%20First%20designs/01%20Hello%20World%20-%20first%20script.py)
Using functions and classes to create a basic app.

### [Buttons and widgets](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/01.%20First%20designs/02.%20Buttons%20and%20widgets.py)
Basic kivy designs, creating buttons and widgets.


    self.top_grid.add_widget(Label(text="Name: "))
    self.name = TextInput(multiline=True)
    self.top_grid.add_widget(self.name)
    

Kivy apps work on a grid based layout. Buttons and widgets are inserted in grids and can be resized by resizing the grid. Default values for girds can be established.

1. Set number of columns:

    ```
    self.cols = 
    ```

2. 
