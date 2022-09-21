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
                                     pady=10) # experiment with these
        self.converter_frame.grid()

        #Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Ubuntu", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # User Instructions (row 1)
        self.user_instructions = Button(self.converter_frame, text="Type the degrees of temperature you'd like to convert, then press either celsius or fahrenheit, of which you'd like to convert your temperature to....",
                                  font="ubuntu 14", wrap=250, justify=LEFT, bg=background_color, padx=10, pady=10,)
        self.user_instructions.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20, font="ubuntu 14")
        self.to_convert_entry.grid(row=2)
