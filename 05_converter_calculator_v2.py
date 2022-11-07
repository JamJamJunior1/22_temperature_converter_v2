from tkinter import *
from functools import partial  # to make sure there aren't any unnecessary windows

import random

# finish later all this stuff below
class Converter:
    def __init__(self, parent):

        # variable formatting
        background_color = "dark turquoise"    # slate blue maybe?

        # Converter Main Screen GUI
        self.converter_frame = Frame(width=300, height=480, bg=background_color,
                                     pady=10)  # experiment with these
        self.converter_frame.grid()

        #Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "10", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # User Instructions (row 1)
        self.user_instructions = Button(self.converter_frame, text="Type the degrees of temperature you'd like to convert, then press either celsius or fahrenheit, of which you'd like to convert your temperature to....",
                                  font="Arial 10 bold", wrap=250, justify=LEFT, bg=background_color, padx=10, pady=10,)
        self.user_instructions.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20, font="Arial 10 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (row 3), orchid3 | khaki (CHANGE THESE, HERE FOR CODES SAKE)
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame, text="To Celsius", font="Arial 10 bold", bg="Khaki1", padx=10, pady=10, command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame, text="To Fahrenheit", font="Arial 10 bold", bg="Orchid1", padx=10, pady=10, command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)
        self.converted_label = Label(self.converter_frame, font="Arial 14 bold", fg="purple", bg=background_color, pady=10, text="Conversion goes here")
        self.converted_label.grid(row=4)

        # History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame, font="Arial 12 bold", fg="purple", bg=background_color, pady=10, text="Calculation History", width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold", fg="purple", bg=background_color, pady=10, text="Help", width=5)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, to):
        print(to)

        error = "#ffafaf"   # change colour for my own thing

        # Retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            print("yep")

        except ValueError:
            print("nope")
        # Check amount is a valid number

        # Convert to F

        # Convert to C

        # Round

        # Display answer

        # Add Answer to list for History
    # This below has the grunt of all the problems with this code. this alone equates to the whole thing not workin so ill have to figure it out
    except ValueError:
        self.converted_label.configure(text="Enter a number", fg="red")
        self.to_convert_entry.configure(bg=error)

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
