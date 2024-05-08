import tkinter as tk

from preprocess_gui import PreprocessPage
from visualize_gui import App

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#282828')

        label = tk.Label(self, text="Welcome to DataViz!", font=('Arial', 40, 'bold'), bg='#282828')
        label.pack(side="top", pady=50)
        
        description_label = tk.Label(self, text='A tool for preprocessing and visualizing data\nCreated for beginners with minimal coding experience', font=('Arial', 14), bg='#282828', fg='white')
        description_label.place(x=465, y=115)
        
        label2 = tk.Label(
            self,
            text='CS 122 Project created by Bryan Melo and Munkh-Erdene Khuderbaatar',
            font=('Arial', 16),
            bg='lightgray',
            fg='black'
        )
        label2.pack(side='bottom', fill='x', pady=5)

        switch_window_button = tk.Button(
            self,
            text="Preprocess Data",
            command=lambda: controller.show_frame(PreprocessPage),
            height=3,
            width=20,
            font=('Arial', 24),
            bg='#282828',
            fg='black',
            bd=0
        )
        switch_window_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        
        switch_window_button2 = tk.Button(
            self,
            text="Visualize Data",
            command=lambda: controller.show_frame(App),
            height=3,
            width=20,
            font=('Arial', 24),
            bg='#282828',
            fg='black',
            bd=0
        )
        switch_window_button2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        