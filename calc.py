import tkinter as tk

FONT_SMALL = ("Arial", "16")
FONT_LARGE = ("Arial", "40", "bold")
DIGITS_FONT_STYlE = ("Arial", "24", "bold")
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
WHITE = "#FFFFFF"


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
        self.create_digit_buttons()

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


    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
