import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


# VS Code will not recognize it, but it will run
from kivy.properties import ObjectProperty

# Import deisgn file
Builder.load_file("updating_labels_design.kv")

class MyLayout(Widget):
    def press(self):
        # Create variables for our widget
        name = self.ids.name_input.text

        # Update the label
        self.ids.name_label.text = f'Hello {name}!'

        # Clear input box
        self.ids.name_input.text = ''




class  MyApp(App): 
    def build(self):
        return MyLayout()


if __name__== '__main__':
    MyApp().run()