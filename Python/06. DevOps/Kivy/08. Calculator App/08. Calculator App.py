import kivy
import re
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

        # Test for error first
        if "Error" in prior:
            prior = ""

        # Determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f"{prior}{button}"

    # Create a function to 
    def math_sign(self, sign):
        prior = self.ids.calc_input.text 

        # 
        self.ids.calc_input.text =f"{prior}{sign}"


    # Create a function to backspace, remove last character
    def remove(self):
        prior = self.ids.calc_input.text

        # Remove the last item in the textbox
        prior = prior[:-1]

        if prior == "":
            prior = "0"
        else:
            pass

        self.ids.calc_input.text = prior

    # Create function to make input positive or negative:
    def pos_neg(self):
        prior = self.ids.calc_input.text

        # Test to see if there is a negative sign
        if "-" in prior:
            self.ids.calc_input.text = f"{prior.replace('-','')}"
        else:
            self.ids.calc_input.text = f"-{prior}"

    # Create a decimal function
    def dot(self):
        prior = self.ids.calc_input.text

        # Split our text box by math sign
        num_list = re.split(r"[+\-*/]", prior)
        
        if "+" in prior and "." not in num_list[-1]:
            prior = f"{prior}."
            self.ids.calc_input.text = prior
        
        elif "." in prior:
            pass

        else:
            # Add decimal to the end of the input
            prior = f"{prior}."

            # Output back to the input
            self.ids.calc_input.text = prior

    def equals(self):
        prior = self.ids.calc_input.text 

        # Error handling
        try:
            # Evaluate the math from the text box
            answer = eval(prior)

            # Output the answer
            answer = str(answer)

            if answer[-2:] == ".0":
                answer = answer[:-2]
            else:
                pass

            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"


class  CalculatorApp(App): 
    def build(self):
        return MyLayout()


if __name__== '__main__':
    CalculatorApp().run() 