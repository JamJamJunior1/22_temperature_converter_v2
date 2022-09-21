from tkinter import *
from functools import partial

import random


class Converter:
    def __init__(self):
        background_colour = "light blue"

        self.convertor_frame = Frame(width=600, height=600, bg=background_colour, pady=10)
        self.convertor_frame.grid()

        self.temp_convertor_label = label(self.convertor_frame, text="Temperature Convertor", font=("Arial", "16", "bold"), bg=background_colour, padx=10, pady=10)
        self.temp_convertor_label.grid(row=0)

        self.help_button = button(self.convertor_frame, text="Help", font=("Arial", "14"), padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")


class Help:
    def __init__(self, partner):

        background = "orange"

        partner.help_button.config(state=DISABLED)
        # finish this later on:
        self.help_box = Toplevel()

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter()
    root.mainloop()

