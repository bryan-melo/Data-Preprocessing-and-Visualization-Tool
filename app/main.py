# Library imports
import tkinter as tk

# Module imports
from preprocess_gui import PreprocessPage
from welcome_gui import WelcomePage
from visualize_gui import App


class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("DataViz")
        self.geometry("1280x800")

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)      
        
        self.frames = {}
        for F in (WelcomePage, PreprocessPage, App):
            frame = F(container, self)
            
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(WelcomePage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        
def main():
    app = MainApp()
    app.mainloop()
    
    
if __name__ == "__main__":
    main()