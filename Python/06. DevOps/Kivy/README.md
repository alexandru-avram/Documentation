# Kivy 

[Kivy Documentation](https://kivy.org/doc/stable/)

### [Hello World](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/hello_world.py)
Using functions and classes to create a basic app.

### [Single File Design](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/single_file_design.py)
Designing a simple app using a single file. We will not use this type, but will use `.kv` files.


## Kivy Packages

    from kivy.app import App


    from kivy.uix.widget import Widget
asfsafsa


## Layouts
I

### [Grid Layout]()

### [Box Layout]()

### [Float Layout]()



2. Widgets
    Types of Widges
   a. Labels
   b. Text Inputs
   c. Buttons
   d. Images

   Inheritance
   Updating Labels
   
APP EXAMPLES:
- Calculator App

## Widgets

### Widget Types

#### Labels

#### Text Inputs

#### Buttons

#### Images

### Widget Inheritance

## App Examples

### Calculator App

]
### [Buttons and widgets](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/01.%20First%20designs/02.%20Buttons%20and%20widgets.py)
Basic kivy designs, creating buttons and widgets. In this example, the design elements are in the same file.


    self.top_grid.add_widget(Label(text="Name: "))
    self.name = TextInput(multiline=True)
    self.top_grid.add_widget(self.name)
    

Kivy apps work on a grid based layout. Buttons and widgets are inserted in grids and can be resized by resizing the grid. Default values for girds can be established.


1. Set number of columns:

    ```
    self.cols = 
    ```

2. Specific size for a grid:

    ```
    self.submit = Button(text="Submit",
    font_size=32,
    size_hint_y = None,  #stop changing the height of the button
    height=50,
    size_hint_x = None,
    width=800
    )
    ```


3. Default sizes for grids:

    ```
    self.row_force_default=True
    self.row_default_height=200
    self.col_force_default=True
    self.col_default_width=400
    ```

### [Basic design pattern](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/02.%20Design%20patterns/03.%20Design%20patterns.py)

[Kivy design file](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/02.%20Design%20patterns/design_file.kv)

The `.kv` design file is the front-end of the application. The main file will keep the application functionality.

Importing a design file

    from kivy.lang import Builder
    from kivy.properties import ObjectProperty
    
    Builder.load_file("design_file.kv")
    name = ObjectProperty(None)

Creating a label for widgets:

    Label:
        text: "Name"
    TextInput:
        id: name
        multiline: False

Creating a button:
       
    Button:
        text: "Submit"
        font_size: 32
        on_press: root.press()

In order to edit the color for buttons or widgets, kivy uses a `RGB - A` model: `red, green, blue and opacity`. They have values between `0 and 1.` For a spcific color, divide the number from a color picker site with **255.0**.

    background_color: (233/255.0, 0, 0, 1)

You can also use `hex color codes`

    #: import utils kivy.utils
    background_color: utils.get_color_from_hex("#eefa00")

The `background_color: ` acts as a multiplier to the texture colour. The default texture is grey, so just setting the background color will give a darker result. To set a plain color, set the background_normal to `''`.



    background_color:''


### [Box Layout](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/03.%20Layout/04.%20Box%20Layout.py)
[Box Layout Design File](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/03.%20Layout/box.kv)

Setting the layout as *box* as opposed to *grid* in the .`kv` design file:

     BoxLayout:
         orientation: "vertical" / "horizontal"

Button and widgets padding and spacing:

    padding: 50
    spacing: 20

Button size and position: (same thing with widgets)

    Button:
        text: "Imi place sa mananc"
        pos_hint: {"center_x": 0.5}
        size_hint: (0.5, 0.5)

### [Widgets Inheritence Properties](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/04.%20Widget%20properties%20inheritance/04.%20Inherit.py)
[Inheritance Design File](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/04.%20Widget%20properties%20inheritance/inherit.kv)

You can set default design elements (such as size or background color) for buttons and widgets by declaring them outside the layout:

    <Button>
        font_size: 32
        background_normal: ""
        background_color: (0.2,0.1,0.5,1)

    <TextInput>
        font_size: 32
        background_normal: ""
        background_color: (0.6,0.2,0.6,0.4)


In order to modify the `<Label>`, use `canvas.before`:

    <Label>
    font_size: 32
    background_color: (0,0.5,1,1)
    
    canvas.before:
        Color:
            rgba: self.background_color
        Rectangle:
            size: self.size
            pos: self.pos
    
    color: (0, 1, 0, 1)
    bold: True
    italic: False
    outline_color: (0,0,0)
    outline_width: 2

To change the background color of the app:

    <MyLayout>
        canvas.before:
            Color:
                rgba: (0,0,0,1)
            Rectangle:
                size: self.size
                pos: self.pos

