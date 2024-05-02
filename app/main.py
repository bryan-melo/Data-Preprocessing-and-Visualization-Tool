# Library imports
import tkinter as tk

from tkinter import ttk
from pathlib import Path

# Module imports
from preprocess_gui import PreprocessPage


class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Tk app")
        self.geometry("1280x800")

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)      
        
        self.frames = {}
        for F in (PreprocessPage, MainPage):
            frame = F(container, self)
            
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(PreprocessPage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Go to the Side Page",
            command=lambda: controller.show_frame(PreprocessPage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

        
def main():
    app = MainApp()
    app.mainloop()
    
    
if __name__ == "__main__":
    main()