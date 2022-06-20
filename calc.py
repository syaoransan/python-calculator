import tkinter as tk

FONT_DEFAULT = ("Arial", 20)
FONT_SMALL = ("Arial", "16")
FONT_LARGE = ("Arial", "40", "bold")
DIGITS_FONT_STYlE = ("Arial", "24", "bold")
LIGHT_GRAY = "#F5F5F5"
LIGHT_BLUE = "#CCEDFF"
LABEL_COLOR = "#25265E"
WHITE = "#FFFFFF"
OFF_WHITE = "#F8FAFF"



class Calculator:

    # Constructor
    def __init__(self):
        # Creating Window
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        self.total_expression = "0"
        self.current_expression = "0"

        # creating Display
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_label()
        self.button_frame = self.create_button_frame()

        self.digits =  {
            7:(1, 1), 8:(1, 2), 9:(1, 3),
            4:(2, 1), 5:(2, 2), 6:(2, 3), 
            1:(3, 1), 2:(3, 2), 3:(3, 3),
            0:(4, 2), '.':(4, 1)
        }
        self.operation = {
            "/" : "\u00F7",
            "*" : "\u00D7",
            "-" : "-",
            "+" : "+"
        }
        self.button_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)


        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    # Display Frame function
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    # Create Display Label
    def create_display_label(self):
        total_label = tk.Label(
            self.display_frame,
            text=self.total_expression,
            anchor=tk.E,
            bg=LIGHT_GRAY,
            fg=LABEL_COLOR,
            padx=24,
            font=FONT_SMALL,
        )
        total_label.pack(expand=True, fill="both")

        label = tk.Label(
            self.display_frame,
            text=self.current_expression,
            anchor=tk.E,
            bg=LIGHT_GRAY,
            fg=LABEL_COLOR,
            padx=24,
            font=FONT_LARGE,
        )
        label.pack(expand=True, fill="both")
        return total_label, label

    # Button Frame function
    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    # Create Digits Button
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(
                self.button_frame,
                text= str(digit),
                bg=WHITE,
                fg= LABEL_COLOR,
                font=DIGITS_FONT_STYlE,
                borderwidth=0
            )
            button.grid(
                row=grid_value[0],
                column=grid_value[1],
                sticky=tk.NSEW
            )
    # Create Operator Buttons
    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operation.items() :
            button = tk.Button(
                    self.button_frame,
                    text=symbol,
                    bg=OFF_WHITE,
                    fg=LABEL_COLOR,
                    font=FONT_DEFAULT,
                    borderwidth=0
                    )
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1
    # Create Equal Button
    def create_equal_button(self) :        
        button = tk.Button(
                self.button_frame,
                text="=",
                bg=LIGHT_BLUE,
                fg=LABEL_COLOR,
                font=FONT_DEFAULT,
                borderwidth=0
                )
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)
    # Create Clear Button
    def create_clear_button(self) :        
        button = tk.Button(
                self.button_frame,
                text="C",
                bg=OFF_WHITE,
                fg=LABEL_COLOR,
                font=FONT_DEFAULT,
                borderwidth=0
                )
        button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    # Create Special Buttons
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equal_button()
        


    def run(self):
        self.window.mainloop()
 

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
