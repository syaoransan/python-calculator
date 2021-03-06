import tkinter as tk
from button import buttonPrint

FONT_SMALL = ("Arial", "16")
FONT_LARGE = ("Arial", "40", "bold")
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

buttonPrint()
class Window:
    def __init__(self) :
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        self.total_expression = "0"
        self.current_expression = "0"
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_label()
        self.button_frame = self.create_button_frame()
        

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
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


    def run(self):
        self.window.mainloop()
