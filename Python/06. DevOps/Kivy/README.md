# Kivy 

[Kivy Documentation](https://kivy.org/doc/stable/)

### [Hello World](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/hello_world.py)
Using functions and classes to create a basic app.

### [Single File Design](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/single_file_design.py)
Designing a simple app using a single file. We will not use this type, but will use `.kv` files.


## Kivy Packages

**Most common kivy imports**

    import kivy
    from kivy.app import App
    from kivy.uix.widget import Widget
    from kivy.lang import Builder
    from kivy.properties import ObjectProperty
    from kivy.core.window import Window

<br>
This line of code is commonly used when building Kivy applications since the App class is a fundamental part of the Kivy framework. By subclassing the App class and defining the `build()` method, you can create the main entry point for your Kivy application.


    from kivy.app import App

<br></br>
You can subclass the Widget class to create your own custom widgets with specific behaviors and appearance. By doing this, you have full control over how your custom widget looks and interacts with the user.


    from kivy.uix.widget import Widget


<br>
Using Builder, you can load Kv language files and apply them to your Kivy application. The `Builder.load_file()` method allows you to load a Kv file and apply its definitions to the current running Kivy application.

    from kivy.lang import Builder


<br>
The ObjectProperty class is a property type in Kivy that allows you to create a reference to a widget or any other object. It's often used in the context of creating custom widgets or when you need to refer to other widgets or objects from your Kivy code.

    from kivy.properties import ObjectProperty


<br>
The Window class in Kivy provides access to various window-related properties and methods, allowing you to interact with the application's main window. You can use the Window class to set the size and position of the window, access input events, retrieve information about the window, and more.

    from kivy.core.window import Window


## Layouts

Import the design `.kv` file.

    Builder.load_file("design_file.kv")

<br>
Default simple structure of a `.py` file based on the **kivy** design framework.

    import kivy
    from kivy.app import App
    from kivy.uix.widget import Widget
    from kivy.lang import Builder
    from kivy.properties import ObjectProperty
    
    # Import the deisgn file
    Builder.load_file("design_file.kv")
    
    class MyLayout(Widget):
        pass
    
    class MyApp(App): 
        def build(self):
            return MyLayout()
    
    if __name__== '__main__':
        MyApp().run()
<br>
* You can set the root size of your app.
* In order to set the spacing between the widgets, specify `padding` and `spacing`.

    Layout:
        # root size
        size: root.width, root.height

        # The space between the buttons
        padding: 50
        spacing: 20



### [Grid Layout](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/Layouts/grid_layout.py)
[Grid layout design kv file](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/Layouts/grid_layout.kv)

        GridLayout:
            cals: 4
            rows: 5

The `GridLayout` requires setting a number of columns and/or rows for your widgets.


### [Box Layout](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/Layouts/box_layout.py)
[Box layout design kv file](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/Layouts/box_layout.kv)

    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height

Specific to `BoxLayout`, you can also choose the orientation. 


### [Float Layout](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/Layouts/float_layout.py)
[Float layout design kv file](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/06.%20DevOps/Kivy/Layouts/float_layout.kv)

    # {"x", "y", "top", "bottom", "left", "right"}
    pos_hint: {"x":0, "top":1}

Apply to a widget in order to determine its possition in the app.


## Widgets

#### Labels

    Label:
        text: "Label Name"
        
#### Text Inputs

    TextInput:
        id: text_input_id
        multiline: False/True

`multiline` can be set to `True` or `False` and determines if you can write on multiple lines in a text input widget.

#### Buttons

    Button:
        text: "Submit"
        on_press: root.press()

`on_press` will be defined as a function in the `.py` file.

#### Images

    Image:
        source: "image_kivy.jpg"

        # Image properties in the app
        allow_strech: True
        keep_ratio: False

### Widget design properties

#### Size

    font_size: 32
    
Setting the font size.

    size_hint: (1, 0.5)
    
The size_hint is a tuple of values used by layouts to manage the sizes of their children. It indicates the size relative to the layout’s size instead of an absolute size (in pixels/points/cm/etc).

#### Color

    background_normal: ""
    background_color: (0.2,0.1,0.5,1)

*  The default texture is grey, so use `background_normal: ""` to set a plain color.
*  In order to edit the color for buttons or widgets, kivy uses a `RGB - A` model: `red, green, blue and opacity`. They have values between `0 and 1.` For a spcific color, divide the number from a color picker site with **255.0**.

        #: import utils kivy.utils
        background_color: utils.get_color_from_hex("#eefa00")

You can also use `hex color codes` by importing the `kivy.utils` package in the `.kv` file.

#### Text formatting

    bold: True
    italic: False

Set to either `True` or `False`

    outline_color: (0,0,0)
    outline_width: 2

Setting the text outliner.
  
### Inheritance

Example of `inheritence`. This should be applied before working on the app layout.

The `canvas` is the root object used for drawing by a widget.

    # Default widget properties
    <Button>
        font_size: 32
        background_normal: ""
        background_color: (0.2,0.1,0.5,1)
    
    <TextInput>
        font_size: 20
        background_normal: ""
        background_color: (0.6,0.2,0.6,0.4)
    
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

    # Start of layout creation
    <MyLayout>
        canvas.before:
            Color:
                rgba: (0,0,0,1)
            Rectangle:
                size: self.size
                pos: self.pos


## App Examples

### [Calculator App](https://github.com/alexandruavram-rusu/Documentation/tree/main/Python/06.%20DevOps/Kivy/App_Examples/calculator_app)
A simple calculator app.
