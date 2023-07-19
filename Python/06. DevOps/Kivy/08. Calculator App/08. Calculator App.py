import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window

# Set the app size
Window.size = (500,700)


# Import deisgn file
Builder.load_file("calculator_design.kv")

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text='0'

# Create a button pressing function
    def button_press(self,button):
        # Create a variable that contains whatever was in the text input
        prior = self.ids.calc_input.text 

        # Determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f"{prior}{button}"

    # Create addition function
    def add(self):
        prior = self.ids.calc_input.text 
        # Slap a + sign to the text
        self.ids.calc_input.text =f"{prior}+"

    # Create subtract function
    def subtract(self):
        prior = self.ids.calc_input.text 
        self.ids.calc_input.text =f"{prior}-"

    # Create multiply function
    def multiply(self):
        prior = self.ids.calc_input.text 
        self.ids.calc_input.text =f"{prior}*"

    # Create divide function
    def divide(self):
        prior = self.ids.calc_input.text 
        self.ids.calc_input.text =f"{prior}/"

    def equals(self):
        prior = self.ids.calc_input.text 

        # Addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0
            # loop through out list
            for number in num_list:
                answer = answer + int(number)

            # print the answer in the text box
            self.ids.calc_input.text = str(answer)
    

class  CalculatorApp(App): 
    def build(self):
        return MyLayout()


if __name__== '__main__':
    CalculatorApp().run()