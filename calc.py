import tkinter as tk


LIGHT_GRAY = "#F5F5F5"
class Calculator :

    #Constructor
    def __init__(self):
        # Creating Window
        self.window = tk.Tk()
        self.window.geometry('375x667')
        self.window.resizable(0,0)
        self.window.title('Calculator')

        # creating Display
        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()





    # Display Frame function
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg= LIGHT_GRAY)
        frame.pack(expand= True, fill="both")
        return frame
    # Button Frame function
    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand= True, fill="both")
        return frame
    
    def run (self):
        self.window.mainloop()


if __name__ == '__main__' :
    calc = Calculator()
    calc.run()