import tkinter as tk
from tkinter import ttk
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

df = pd.read_csv("https://raw.githubusercontent.com/csbfx/advpy122-data/master/Pokemon.csv")
def plot_boxplot1(parent_frame, x, y, title=None):
    for widget in parent_frame.winfo_children():
        widget.destroy()
    errorLabel = tk.Label(parent_frame, text="", fg="red", bg="lightblue", font=("Helvetica", 20))
    try:
        plot = sns.catplot(
            data=df,
            x=x,
            y=y,
            kind='box',
            legend=False
        )
        if(title is not None):
            plt.title(title, y=0.98)
        plt.xticks(rotation=45)
        fig = plot.figure
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(anchor="center", fill=tk.BOTH, expand=True, padx=10, pady=10, ipadx=5, ipady=5)
    except Exception as ex:
        errorLabel.pack(side="top", padx=10, pady=10)
        errorLabel.config(text=f"Error: {ex}")

def plot_boxplot2(parent_frame, x, y, hue, title=None):
    for widget in parent_frame.winfo_children():
        widget.destroy()
    errorLabel = tk.Label(parent_frame, text="", fg="red", bg="lightblue", font=("Helvetica", 20))
    try:
        plot = sns.catplot(
            data=df,
            x=x,
            y=y,
            hue=hue,
            kind='box',
            legend=False
        )
        if(title is not None):
            plt.title(title)
        plt.xticks(rotation=45)
        fig = plot.figure
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(anchor="center", fill=tk.BOTH, expand=True, padx=10, pady=10, ipadx=5, ipady=5)
    except Exception as ex:
        errorLabel.pack(side="top", padx=10, pady=10)
        errorLabel.config(text=f"Error: {ex}")

def plot_boxplot3(parent_frame, x, y, hue, col, title=None):
    for widget in parent_frame.winfo_children():
        widget.destroy()
    errorLabel = tk.Label(parent_frame, text="", fg="red", bg="lightblue", font=("Helvetica", 20))
    try:
        plot = sns.catplot(
            data=df,
            x=x,
            y=y,
            hue=hue,
            col=col,
            kind='box',
            legend=True
        )
        if(title is not None):
            plt.title(title)
        plot.set_xticklabels(rotation=45)
        fig = plot.figure
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(anchor="center", fill=tk.BOTH, expand=True, padx=10, pady=10, ipadx=5, ipady=5)
    except Exception as ex:
        errorLabel.pack(side="top", padx=10, pady=10)
        errorLabel.config(text=f"Error: {ex}")

def plot_stripplot1(parent_frame, x, y, title=None):
    for widget in parent_frame.winfo_children():
        widget.destroy()
    errorLabel = tk.Label(parent_frame, text="", fg="red", bg="lightblue", font=("Helvetica", 20))
    try:
        plot = sns.catplot(
            data=df,
            x=x,
            y=y,
            aspect=1,
            height=10,
            jitter=0.3,
            palette="Set2",
            kind='strip',
            legend=False
        )
        if(title is not None):
            plt.title(title, y=0.98)
        plt.xticks(rotation=45)
        fig = plot.figure
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(anchor="center", fill=tk.BOTH, expand=True, padx=10, pady=10, ipadx=5, ipady=5)
    except Exception as ex:
        errorLabel.pack(side="top", padx=10, pady=10)
        errorLabel.config(text=f"Error: {ex}")

def plot_stripplot2(parent_frame, x, y, hue, title=None):
    for widget in parent_frame.winfo_children():
        widget.destroy()
    errorLabel = tk.Label(parent_frame, text="", fg="red", bg="lightblue", font=("Helvetica", 20))
    try:
        plot = sns.catplot(
            data=df,
            x=x,
            y=y,
            hue=hue,
            aspect=1,
            height=10,
            jitter=0.3,
            palette="Set2",
            kind='strip',
            legend=False
        )
        if(title is not None):
            plt.title(title, y=0.98)
        plt.xticks(rotation=45)
        fig = plot.figure
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(anchor="center", fill=tk.BOTH, expand=True, padx=10, pady=10, ipadx=5, ipady=5)
    except Exception as ex:
        errorLabel.pack(side="top", padx=10, pady=10)
        errorLabel.config(text=f"Error: {ex}")

def plot_stripplot3(parent_frame, x, y, hue, col, title=None):
    for widget in parent_frame.winfo_children():
        widget.destroy()
    errorLabel = tk.Label(parent_frame, text="", fg="red", bg="lightblue", font=("Helvetica", 20))
    try:
        plot = sns.catplot(
            data=df,
            x=x,
            y=y,
            hue=hue,
            col=col,
            aspect=1,
            height=10,
            jitter=0.3,
            palette="Set2",
            kind='strip',
            legend=False
        )
        if(title is not None):
            plt.title(title, y=0.98)
        plot.set_xticklabels(rotation=45)
        fig = plot.figure
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(anchor="center", fill=tk.BOTH, expand=True, padx=10, pady=10, ipadx=5, ipady=5)
    except Exception as ex:
        errorLabel.pack(side="top", padx=10, pady=10)
        errorLabel.config(text=f"Error: {ex}")

def plot_violinplot1(parent_frame, x, y, scale, cut, bw, title=None):
    for widget in parent_frame.winfo_children():
        widget.destroy()
    errorLabel = tk.Label(parent_frame, text="", fg="red", bg="lightblue", font=("Helvetica", 20))
    try:
        if(scale=="count"):
            plot = sns.catplot(
                data=df,
                x=x,
                y=y,
                cut=cut,
                bw=bw,
                scale="count",
                kind='violin'
            )
        else:
            plot = sns.catplot(
                data=df,
                x=x,
                y=y,
                cut=cut,
                bw=bw,
                kind='violin'
            )
        if(title is not None):
            plt.title(title, y=0.98)
        plt.xticks(rotation=45)
        fig = plot.figure
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(anchor="center", fill=tk.BOTH, expand=True, padx=10, pady=10, ipadx=5, ipady=5)
    except Exception as ex:
        errorLabel.pack(side="top", padx=10, pady=10)
        errorLabel.config(text=f"Error: {ex}")

def plot_violinplot2(parent_frame, x, y, hue, scale, cut, bw, title=None):
    for widget in parent_frame.winfo_children():
        widget.destroy()
    errorLabel = tk.Label(parent_frame, text="", fg="red", bg="lightblue", font=("Helvetica", 20))
    try:
        if(scale == "count"):
            plot = sns.catplot(
                data=df,
                x=x,
                y=y,
                cut=cut,
                bw=bw,
                hue=hue,
                scale="count",
                kind='violin'
            )
        else:
            plot = sns.catplot(
                data=df,
                x=x,
                y=y,
                cut=cut,
                bw=bw,
                hue=hue,
                kind='violin'
            )
        if(title is not None):
            plt.title(title, y=0.98)
        plt.xticks(rotation=45)
        fig = plot.figure
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(anchor="center", fill=tk.BOTH, expand=True, padx=10, pady=10, ipadx=5, ipady=5)
    except Exception as ex:
        errorLabel.pack(side="top", padx=10, pady=10)
        errorLabel.config(text=f"Error: {ex}")

def plot_scatterplot1(parent_frame, x, y, title=None):
    for widget in parent_frame.winfo_children():
        widget.destroy()
    errorLabel = tk.Label(parent_frame, text="", fg="red", bg="lightblue", font=("Helvetica", 20))
    try:
        plot = sns.relplot(
            data=df,
            x=x,
            y=y
        )
        if(title is not None):
            plt.title(title, y=0.98)
        plot.set_xticklabels(rotation=45)
        plot.set_yticklabels(rotation=45)
        fig = plot.figure
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(anchor="center", fill=tk.BOTH, expand=True, padx=10, pady=10, ipadx=5, ipady=5)
    except Exception as ex:
        errorLabel.pack(side="top", padx=10, pady=10)
        errorLabel.config(text=f"Error: {ex}")

def plot_scatterplot2(parent_frame, x, y, hue, palette, title=None):
    for widget in parent_frame.winfo_children():
        widget.destroy()
    errorLabel = tk.Label(parent_frame, text="", fg="red", bg="lightblue", font=("Helvetica", 20))
    try:
        plot = sns.relplot(
            data=df,
            x=x,
            y=y,
            hue=hue,
            palette=palette
        )
        if(title is not None):
            plt.title(title, y=0.98)
        plot.set_xticklabels(rotation=45)
        plot.set_yticklabels(rotation=45)
        fig = plot.figure
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(anchor="center", fill=tk.BOTH, expand=True, padx=10, pady=10, ipadx=5, ipady=5)
    except Exception as ex:
        errorLabel.pack(side="top", padx=10, pady=10)
        errorLabel.config(text=f"Error: {ex}")

def plot_regressionplot1(parent_frame, x, y, pol_order, ci,size, color, title=None):
    for widget in parent_frame.winfo_children():
        widget.destroy()
    errorLabel = tk.Label(parent_frame, text="", fg="red", bg="lightblue", font=("Helvetica", 20))
    try:
        plot = sns.lmplot(
            data=df,
            x=x,
            y=y,
            order=pol_order,
            ci=ci,
            scatter_kws={'s':size, 'color':color}
        )
        if(title is not None):
            plt.title(title, y=0.98)
        plt.xticks(rotation=45)
        fig = plot.figure
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(anchor="center", fill=tk.BOTH, expand=True, padx=10, pady=10, ipadx=5, ipady=5)
    except Exception as ex:
        errorLabel.pack(side="top", padx=10, pady=10)
        errorLabel.config(text=f"Error: {ex}")

def plot_barplot1(parent_frame, x, order):
    for widget in parent_frame.winfo_children():
        widget.destroy()
    errorLabel = tk.Label(parent_frame, text="", fg="red", bg="lightblue", font=("Helvetica", 20))
    try:
        plot = sns.catplot(
            data=df,
            x=x,
            kind="count",
            order=df[order].value_counts().index,
            color='darkblue'
        )
        plt.xticks(rotation=45)
        fig = plot.figure
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(anchor="center", fill=tk.BOTH, expand=True, padx=10, pady=10, ipadx=5, ipady=5)
    except Exception as ex:
        errorLabel.pack(side="top", padx=10, pady=10)
        errorLabel.config(text=f"Error: {ex}")

class App(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.config(bg='navy')
        #add canvas
        self.canvas = MyCanvas(self, 410, 800)
        self.canvas.to_pack('left',False, 'y', 10, 10)
        #add scrollbar
        self.scrollbar = MyScrollbar(self, tk.VERTICAL, self.canvas.yview)
        self.scrollbar.to_pack('left', False, 'y', 5, 10)
        #add Notebook(tabs)
        self.notebook = MyNotebook(self.canvas, 410, 800)
        self.boxplot_tab = MyFrame(self.notebook, 200, 800, 'lightblue', 'solid', 1)
        self.stripplot_tab = MyFrame(self.notebook, 200, 800, 'lightblue', 'solid', 1)
        self.violinplot_tab = MyFrame(self.notebook, 200, 800, 'lightblue', 'solid', 1)
        self.scatterplot_tab = MyFrame(self.notebook, 200, 800, 'lightblue', 'solid', 1)
        self.regressionplot_tab = MyFrame(self.notebook, 200, 800, 'lightblue', 'solid', 1)
        self.barplot_tab = MyFrame(self.notebook, 200, 800, 'lightblue', 'solid', 1)
        self.notebook.add_tab(self.boxplot_tab, "BoxPlot")
        self.notebook.add_tab(self.stripplot_tab, "StripPlot")
        self.notebook.add_tab(self.violinplot_tab, "ViolinPlot")
        self.notebook.add_tab(self.scatterplot_tab, "ScatterPlot")
        self.notebook.add_tab(self.regressionplot_tab, "RegressionPlot")
        self.notebook.add_tab(self.barplot_tab, "BarPlot")
        self.notebook.to_pack('top', False, 'y', 5, 5)
        #add window inside the canvas
        self.canvas.add_window((0,0), self.notebook, tk.NW)
        #update notebook
        self.notebook.update()
        self.canvas.configurate(self.canvas.bbox('all'))
        #Add visualization frame
        self.visualization_frame = MyFrame(self, 1000, 500, 'lightblue', 'solid', 1)
        self.visualization_frame.to_pack('left', True, 'both', 10, 10)

#Box Plot Widgets    
    #Option 1 Box Plot Frame
        self.boxplot1_frame = MyFrame(self.boxplot_tab, 300, 300, 'white', 'solid', 1)
        self.boxplot1_frame.to_pack('top', False, "both", 10, 10)
        #Adding X-Axis Widgets
        self.label_x1_boxplot_tab = MyLabel(self.boxplot1_frame, "X-Axis:")
        self.label_x1_boxplot_tab.to_grid(0, 0, 10, 10)
        self.selected_x1_boxplot_tab = MyStringVar(self.boxplot1_frame)
        self.menu_x1_boxplot_tab = MyOptionMenu(self.boxplot1_frame, self.selected_x1_boxplot_tab, df.columns) 
        self.menu_x1_boxplot_tab.to_grid(0, 1, 10, 10)
        #Adding Y-Axis Widgets
        self.label_y1_boxplot_tab = MyLabel(self.boxplot1_frame, "Y-Axis:")
        self.label_y1_boxplot_tab.to_grid(1, 0, 10, 10)
        self.selected_y1_boxplot_tab = MyStringVar(self.boxplot1_frame)
        self.menu_y1_boxplot_tab = MyOptionMenu(self.boxplot1_frame, self.selected_y1_boxplot_tab, df.columns) 
        self.menu_y1_boxplot_tab.to_grid(1, 1, 10, 10)
        #Adding Title Widgets
        self.label_title1_boxplot_tab = MyLabel(self.boxplot1_frame, "Title(Optional):")
        self.label_title1_boxplot_tab.to_grid(2, 0, 10, 10)
        self.entry_title1_boxplot_tab = MyEntry(self.boxplot1_frame)
        self.entry_title1_boxplot_tab.to_grid(2, 1, 10, 10)
        #Adding Button For Option 1 Frame
        self.button1_boxplot_tab = MyButton(self.boxplot1_frame, "Plot", lambda: plot_boxplot1(self.visualization_frame, self.selected_x1_boxplot_tab.get(), self.selected_y1_boxplot_tab.get(), self.entry_title1_boxplot_tab.get()))
        self.button1_boxplot_tab.to_grid(3, 1, 10, 10)
    #Option 2 Box Plot Frame   
        self.boxplot2_frame = MyFrame(self.boxplot_tab, 300, 300, 'white', 'solid', 1)
        self.boxplot2_frame.to_pack('top', False, "both", 10, 10)
        #Adding X-Axis Widgets
        self.label_x2_boxplot_tab = MyLabel(self.boxplot2_frame, "X-axis:")
        self.label_x2_boxplot_tab.to_grid(0, 0, 10, 10)
        self.selected_x2_boxplot_tab = MyStringVar(self.boxplot2_frame)
        self.menu_x2_boxplot_tab = MyOptionMenu(self.boxplot2_frame, self.selected_x2_boxplot_tab, df.columns) 
        self.menu_x2_boxplot_tab.to_grid(0, 1, 10, 10)
        #Adding Y-Axis Widgets
        self.label_y2_boxplot_tab = MyLabel(self.boxplot2_frame, "Y-axis:")
        self.label_y2_boxplot_tab.to_grid(1, 0, 10, 10)
        self.selected_y2_boxplot_tab = MyStringVar(self.boxplot2_frame)
        self.menu_y2_boxplot_tab = MyOptionMenu(self.boxplot2_frame, self.selected_y2_boxplot_tab, df.columns) 
        self.menu_y2_boxplot_tab.to_grid(1, 1, 10, 10)
        #Adding Title Widgets
        self.label_title2_boxplot_tab = MyLabel(self.boxplot2_frame, "Title(Optional):")
        self.label_title2_boxplot_tab.to_grid(2, 0, 10, 10)
        self.entry_title2_boxplot_tab = MyEntry(self.boxplot2_frame)
        self.entry_title2_boxplot_tab.to_grid(2, 1, 10, 10)
        #Adding Hue
        self.label_hue2_boxplot_tab = MyLabel(self.boxplot2_frame, "Hue:")
        self.label_hue2_boxplot_tab.to_grid(3, 0, 10, 10)
        self.selected_hue2_boxplot_tab = MyStringVar(self.boxplot2_frame)
        self.menu_hue2_boxplot_tab = MyOptionMenu(self.boxplot2_frame, self.selected_hue2_boxplot_tab, df.columns) 
        self.menu_hue2_boxplot_tab.to_grid(3, 1, 10, 10)
        #Adding Button For Option 2 Frame
        self.button2_boxplot_tab = MyButton(self.boxplot2_frame, "Plot", lambda: plot_boxplot2(self.visualization_frame, self.selected_x2_boxplot_tab.get(), self.selected_y2_boxplot_tab.get(), self.selected_hue2_boxplot_tab.get(), self.entry_title2_boxplot_tab.get()))
        self.button2_boxplot_tab.to_grid(4, 1, 10, 10)
    #Option 3 Box Plot Frame  
        self.boxplot3_frame = MyFrame(self.boxplot_tab, 300, 300, 'white', 'solid', 1)
        self.boxplot3_frame.to_pack('top', False, "both", 10, 10)
        #Adding X-Axis Widgets
        self.label_x3_boxplot_tab = MyLabel(self.boxplot3_frame, "X-Axis:")
        self.label_x3_boxplot_tab.to_grid(0, 0, 10, 10)
        self.selected_x3_boxplot_tab = MyStringVar(self.boxplot3_frame)
        self.menu_x3_boxplot_tab = MyOptionMenu(self.boxplot3_frame, self.selected_x3_boxplot_tab, df.columns) 
        self.menu_x3_boxplot_tab.to_grid(0, 1, 10, 10)
        #Adding Y-Axis Widgets
        self.label_y3_boxplot_tab = MyLabel(self.boxplot3_frame, "Y-Axis:")
        self.label_y3_boxplot_tab.to_grid(1, 0, 10, 10)
        self.selected_y3_boxplot_tab = MyStringVar(self.boxplot3_frame)
        self.menu_y3_boxplot_tab = MyOptionMenu(self.boxplot3_frame, self.selected_y3_boxplot_tab, df.columns) 
        self.menu_y3_boxplot_tab.to_grid(1, 1, 10, 10)
        #Adding Title Widgets
        self.label_title3_boxplot_tab = MyLabel(self.boxplot3_frame, "Title(Optional):")
        self.label_title3_boxplot_tab.to_grid(2, 0, 10, 10)
        self.entry_title3_boxplot_tab = MyEntry(self.boxplot3_frame)
        self.entry_title3_boxplot_tab.to_grid(2, 1, 10, 10)
        #Adding Hue
        self.label_hue3_boxplot_tab = MyLabel(self.boxplot3_frame, "Hue:")
        self.label_hue3_boxplot_tab.to_grid(3, 0, 10, 10)
        self.selected_hue3_boxplot_tab = MyStringVar(self.boxplot3_frame)
        self.menu_hue3_boxplot_tab = MyOptionMenu(self.boxplot3_frame, self.selected_hue3_boxplot_tab, df.columns) 
        self.menu_hue3_boxplot_tab.to_grid(3, 1, 10, 10)
        #Adding Col
        self.label_col3_boxplot_tab = MyLabel(self.boxplot3_frame, "Col:")
        self.label_col3_boxplot_tab.to_grid(4, 0, 10, 10)
        self.selected_col3_boxplot_tab = MyStringVar(self.boxplot3_frame)
        self.menu_col3_boxplot_tab = MyOptionMenu(self.boxplot3_frame, self.selected_col3_boxplot_tab, df.columns) 
        self.menu_col3_boxplot_tab.to_grid(4, 1, 10, 10)
        #Adding Button For Option 3 Frame
        self.button3_boxplot_tab = MyButton(self.boxplot3_frame, "Plot", lambda: plot_boxplot3(self.visualization_frame, self.selected_x3_boxplot_tab.get(), self.selected_y3_boxplot_tab.get(), self.selected_hue3_boxplot_tab.get(), self.selected_col3_boxplot_tab.get(), self.entry_title3_boxplot_tab.get()))
        self.button3_boxplot_tab.to_grid(5, 1, 10, 10)

#Strip Plot Widgets
    #Option 1 Strip Plot Frame
        self.stripplot1_frame = MyFrame(self.stripplot_tab, 300, 300, 'white', 'solid', 1)
        self.stripplot1_frame.to_pack('top', False, "both", 10, 10)
        #Adding X-Axis Widgets
        self.label_x1_stripplot_tab = MyLabel(self.stripplot1_frame, "X-Axis:")
        self.label_x1_stripplot_tab.to_grid(0, 0, 10, 10)
        self.selected_x1_stripplot_tab = MyStringVar(self.stripplot1_frame)
        self.menu_x1_stripplot_tab = MyOptionMenu(self.stripplot1_frame, self.selected_x1_stripplot_tab, df.columns) 
        self.menu_x1_stripplot_tab.to_grid(0, 1, 10, 10)
        #Adding Y-Axis Widgets
        self.label_y1_stripplot_tab = MyLabel(self.stripplot1_frame, "Y-Axis:")
        self.label_y1_stripplot_tab.to_grid(1, 0, 10, 10)
        self.selected_y1_stripplot_tab = MyStringVar(self.stripplot1_frame)
        self.menu_y1_stripplot_tab = MyOptionMenu(self.stripplot1_frame, self.selected_y1_stripplot_tab, df.columns) 
        self.menu_y1_stripplot_tab.to_grid(1, 1, 10, 10)
        #Adding Title Widgets
        self.label_title1_stripplot_tab = MyLabel(self.stripplot1_frame, "Title(Optional):")
        self.label_title1_stripplot_tab.to_grid(2, 0, 10, 10)
        self.entry_title1_stripplot_tab = MyEntry(self.stripplot1_frame)
        self.entry_title1_stripplot_tab.to_grid(2, 1, 10, 10)
        #Adding Button For Option 1 Frame
        self.button1_stripplot_tab = MyButton(self.stripplot1_frame, "Plot", lambda: plot_stripplot1(self.visualization_frame, self.selected_x1_stripplot_tab.get(), self.selected_y1_stripplot_tab.get(), self.entry_title1_stripplot_tab.get()))
        self.button1_stripplot_tab.to_grid(3, 1, 10, 10)
    #Option 2 Strip Plot Frame   
        self.stripplot2_frame = MyFrame(self.stripplot_tab, 300, 300, 'white', 'solid', 1)
        self.stripplot2_frame.to_pack('top', False, "both", 10, 10)
        #Adding X-Axis Widgets
        self.label_x2_stripplot_tab = MyLabel(self.stripplot2_frame, "X-axis:")
        self.label_x2_stripplot_tab.to_grid(0, 0, 10, 10)
        self.selected_x2_stripplot_tab = MyStringVar(self.stripplot2_frame)
        self.menu_x2_stripplot_tab = MyOptionMenu(self.stripplot2_frame, self.selected_x2_stripplot_tab, df.columns) 
        self.menu_x2_stripplot_tab.to_grid(0, 1, 10, 10)
        #Adding Y-Axis Widgets
        self.label_y2_stripplot_tab = MyLabel(self.stripplot2_frame, "Y-axis:")
        self.label_y2_stripplot_tab.to_grid(1, 0, 10, 10)
        self.selected_y2_stripplot_tab = MyStringVar(self.stripplot2_frame)
        self.menu_y2_stripplot_tab = MyOptionMenu(self.stripplot2_frame, self.selected_y2_stripplot_tab, df.columns) 
        self.menu_y2_stripplot_tab.to_grid(1, 1, 10, 10)
        #Adding Title Widgets
        self.label_title2_stripplot_tab = MyLabel(self.stripplot2_frame, "Title(Optional):")
        self.label_title2_stripplot_tab.to_grid(2, 0, 10, 10)
        self.entry_title2_stripplot_tab = MyEntry(self.stripplot2_frame)
        self.entry_title2_stripplot_tab.to_grid(2, 1, 10, 10)
        #Adding Hue
        self.label_hue2_stripplot_tab = MyLabel(self.stripplot2_frame, "Hue:")
        self.label_hue2_stripplot_tab.to_grid(3, 0, 10, 10)
        self.selected_hue2_stripplot_tab = MyStringVar(self.stripplot2_frame)
        self.menu_hue2_stripplot_tab = MyOptionMenu(self.stripplot2_frame, self.selected_hue2_stripplot_tab, df.columns) 
        self.menu_hue2_stripplot_tab.to_grid(3, 1, 10, 10)
        
        #Adding Button For Option 2 Frame
        self.button2_stripplot_tab = MyButton(self.stripplot2_frame, "Plot", lambda: plot_stripplot2(self.visualization_frame, self.selected_x2_stripplot_tab.get(), self.selected_y2_stripplot_tab.get(), self.selected_hue2_stripplot_tab.get(), self.entry_title2_stripplot_tab.get()))
        self.button2_stripplot_tab.to_grid(4, 1, 10, 10)
    #Option 3 Strip Plot Frame  
        self.stripplot3_frame = MyFrame(self.stripplot_tab, 300, 300, 'white', 'solid', 1)
        self.stripplot3_frame.to_pack('top', False, "both", 10, 10)
        #Adding X-Axis Widgets
        self.label_x3_stripplot_tab = MyLabel(self.stripplot3_frame, "X-Axis:")
        self.label_x3_stripplot_tab.to_grid(0, 0, 10, 10)
        self.selected_x3_stripplot_tab = MyStringVar(self.stripplot3_frame)
        self.menu_x3_stripplot_tab = MyOptionMenu(self.stripplot3_frame, self.selected_x3_stripplot_tab, df.columns) 
        self.menu_x3_stripplot_tab.to_grid(0, 1, 10, 10)
        #Adding Y-Axis Widgets
        self.label_y3_stripplot_tab = MyLabel(self.stripplot3_frame, "Y-Axis:")
        self.label_y3_stripplot_tab.to_grid(1, 0, 10, 10)
        self.selected_y3_stripplot_tab = MyStringVar(self.stripplot3_frame)
        self.menu_y3_stripplot_tab = MyOptionMenu(self.stripplot3_frame, self.selected_y3_stripplot_tab, df.columns) 
        self.menu_y3_stripplot_tab.to_grid(1, 1, 10, 10)
        #Adding Title Widgets
        self.label_title3_stripplot_tab = MyLabel(self.stripplot3_frame, "Title(Optional):")
        self.label_title3_stripplot_tab.to_grid(2, 0, 10, 10)
        self.entry_title3_stripplot_tab = MyEntry(self.stripplot3_frame)
        self.entry_title3_stripplot_tab.to_grid(2, 1, 10, 10)
        #Adding Hue
        self.label_hue3_stripplot_tab = MyLabel(self.stripplot3_frame, "Hue:")
        self.label_hue3_stripplot_tab.to_grid(3, 0, 10, 10)
        self.selected_hue3_stripplot_tab = MyStringVar(self.stripplot3_frame)
        self.menu_hue3_stripplot_tab = MyOptionMenu(self.stripplot3_frame, self.selected_hue3_stripplot_tab, df.columns) 
        self.menu_hue3_stripplot_tab.to_grid(3, 1, 10, 10)
        #Adding Col
        self.label_col3_stripplot_tab = MyLabel(self.stripplot3_frame, "Col:")
        self.label_col3_stripplot_tab.to_grid(4, 0, 10, 10)
        self.selected_col3_stripplot_tab = MyStringVar(self.stripplot3_frame)
        self.menu_col3_stripplot_tab = MyOptionMenu(self.stripplot3_frame, self.selected_col3_stripplot_tab, df.columns) 
        self.menu_col3_stripplot_tab.to_grid(4, 1, 10, 10)
        #Adding Button For Option 3 Frame
        self.button3_stripplot_tab = MyButton(self.stripplot3_frame, "Plot", lambda: plot_stripplot3(self.visualization_frame, self.selected_x3_stripplot_tab.get(), self.selected_y3_stripplot_tab.get(), self.selected_hue3_stripplot_tab.get(), self.selected_col3_stripplot_tab.get(), self.entry_title3_stripplot_tab.get()))
        self.button3_stripplot_tab.to_grid(5, 1, 10, 10)

#Violin Plot Widgets
    #Option 1 Violin Plot Frame
        self.violinplot1_frame = MyFrame(self.violinplot_tab, 300, 300, 'white', 'solid', 1)
        self.violinplot1_frame.to_pack('top', False, "both", 10, 10)
        #Adding X-Axis Widgets
        self.label_x1_violinplot_tab = MyLabel(self.violinplot1_frame, "X-Axis:")
        self.label_x1_violinplot_tab.to_grid(0, 0, 10, 10)
        self.selected_x1_violinplot_tab = MyStringVar(self.violinplot1_frame)
        self.menu_x1_violinplot_tab = MyOptionMenu(self.violinplot1_frame, self.selected_x1_violinplot_tab, df.columns) 
        self.menu_x1_violinplot_tab.to_grid(0, 1, 10, 10)
        #Adding Y-Axis Widgets
        self.label_y1_violinplot_tab = MyLabel(self.violinplot1_frame, "Y-Axis:")
        self.label_y1_violinplot_tab.to_grid(1, 0, 10, 10)
        self.selected_y1_violinplot_tab = MyStringVar(self.violinplot1_frame)
        self.menu_y1_violinplot_tab = MyOptionMenu(self.violinplot1_frame, self.selected_y1_violinplot_tab, df.columns) 
        self.menu_y1_violinplot_tab.to_grid(1, 1, 10, 10)
        #Adding Title Widgets
        self.label_title1_violinplot_tab = MyLabel(self.violinplot1_frame, "Title(Optional):")
        self.label_title1_violinplot_tab.to_grid(2, 0, 10, 10)
        self.entry_title1_violinplot_tab = MyEntry(self.violinplot1_frame)
        self.entry_title1_violinplot_tab.to_grid(2, 1, 10, 10)
        #Adding Cut Widgets
        self.label_cut1_violinplot_tab = MyLabel(self.violinplot1_frame, "Cut(0-1):")
        self.label_cut1_violinplot_tab.to_grid(3, 0, 10, 10)
        self.entry_cut1_violinplot_tab = MyEntry(self.violinplot1_frame)
        self.entry_cut1_violinplot_tab.to_grid(3, 1, 10, 10)
        #Adding BW Widgets
        self.label_bw1_violinplot_tab = MyLabel(self.violinplot1_frame, "Bandwidth(0-1):")
        self.label_bw1_violinplot_tab.to_grid(4, 0, 10, 10)
        self.entry_bw1_violinplot_tab = MyEntry(self.violinplot1_frame)
        self.entry_bw1_violinplot_tab.to_grid(4, 1, 10, 10)
        #Adding Scale Widgets
        scale = ["count", "None"]
        self.label_scale1_violinplot_tab = MyLabel(self.violinplot1_frame, "Scale:")
        self.label_scale1_violinplot_tab.to_grid(5, 0, 10, 10)
        self.selected_scale1_violinplot_tab = MyStringVar(self.violinplot1_frame)
        self.menu_scale1_violinplot_tab = MyOptionMenu(self.violinplot1_frame, self.selected_scale1_violinplot_tab, scale) 
        self.menu_scale1_violinplot_tab.to_grid(5, 1, 10, 10)
        #Adding Button For Option 1 Frame
        self.button1_violinplot_tab = MyButton(self.violinplot1_frame, "Plot", lambda: plot_violinplot1(self.visualization_frame, self.selected_x1_violinplot_tab.get(), self.selected_y1_violinplot_tab.get(), self.selected_scale1_violinplot_tab.get(), float(self.entry_cut1_violinplot_tab.get()), float(self.entry_bw1_violinplot_tab.get()), self.entry_title1_violinplot_tab.get()))
        self.button1_violinplot_tab.to_grid(6, 1, 10, 10)
    #Option 2 Violin Plot Frame
        self.violinplot2_frame = MyFrame(self.violinplot_tab, 300, 300, 'white', 'solid', 1)
        self.violinplot2_frame.to_pack('top', False, "both", 10, 10)
        #Adding X-Axis Widgets
        self.label_x2_violinplot_tab = MyLabel(self.violinplot2_frame, "X-Axis:")
        self.label_x2_violinplot_tab.to_grid(0, 0, 10, 10)
        self.selected_x2_violinplot_tab = MyStringVar(self.violinplot2_frame)
        self.menu_x2_violinplot_tab = MyOptionMenu(self.violinplot2_frame, self.selected_x2_violinplot_tab, df.columns) 
        self.menu_x2_violinplot_tab.to_grid(0, 1, 10, 10)
        #Adding Y-Axis Widgets
        self.label_y2_violinplot_tab = MyLabel(self.violinplot2_frame, "Y-Axis:")
        self.label_y2_violinplot_tab.to_grid(1, 0, 10, 10)
        self.selected_y2_violinplot_tab = MyStringVar(self.violinplot2_frame)
        self.menu_y2_violinplot_tab = MyOptionMenu(self.violinplot2_frame, self.selected_y2_violinplot_tab, df.columns) 
        self.menu_y2_violinplot_tab.to_grid(1, 1, 10, 10)
        #Adding Title Widgets
        self.label_title2_violinplot_tab = MyLabel(self.violinplot2_frame, "Title(Optional):")
        self.label_title2_violinplot_tab.to_grid(2, 0, 10, 10)
        self.entry_title2_violinplot_tab = MyEntry(self.violinplot2_frame)
        self.entry_title2_violinplot_tab.to_grid(2, 1, 10, 10)
        #Adding Cut Widgets
        self.label_cut2_violinplot_tab = MyLabel(self.violinplot2_frame, "Cut(0-1):")
        self.label_cut2_violinplot_tab.to_grid(3, 0, 10, 10)
        self.entry_cut2_violinplot_tab = MyEntry(self.violinplot2_frame)
        self.entry_cut2_violinplot_tab.to_grid(3, 1, 10, 10)
        #Adding BW Widgets
        self.label_bw2_violinplot_tab = MyLabel(self.violinplot2_frame, "Bandwidth(0-1):")
        self.label_bw2_violinplot_tab.to_grid(4, 0, 10, 10)
        self.entry_bw2_violinplot_tab = MyEntry(self.violinplot2_frame)
        self.entry_bw2_violinplot_tab.to_grid(4, 1, 10, 10)
        #Adding Hue Widgets
        self.label_hue2_violinplot_tab = MyLabel(self.violinplot2_frame, "Hue:")
        self.label_hue2_violinplot_tab.to_grid(5, 0, 10, 10)
        self.selected_hue2_violinplot_tab = MyStringVar(self.violinplot2_frame)
        self.menu_hue2_violinplot_tab = MyOptionMenu(self.violinplot2_frame, self.selected_hue2_violinplot_tab, df.columns) 
        self.menu_hue2_violinplot_tab.to_grid(5, 1, 10, 10)
        #Adding Scale Widgets
        scale = ["count", "None"]
        self.label_scale2_violinplot_tab = MyLabel(self.violinplot2_frame, "Scale:")
        self.label_scale2_violinplot_tab.to_grid(6, 0, 10, 10)
        self.selected_scale2_violinplot_tab = MyStringVar(self.violinplot2_frame)
        self.menu_scale2_violinplot_tab = MyOptionMenu(self.violinplot2_frame, self.selected_scale2_violinplot_tab, scale) 
        self.menu_scale2_violinplot_tab.to_grid(6, 1, 10, 10)
        #Adding Button For Option 2 Frame
        self.button2_violinplot_tab = MyButton(self.violinplot2_frame, "Plot", lambda: plot_violinplot2(self.visualization_frame, self.selected_x2_violinplot_tab.get(), self.selected_y2_violinplot_tab.get(), self.selected_hue2_violinplot_tab.get(), self.selected_scale2_violinplot_tab.get(), float(self.entry_cut2_violinplot_tab.get()), float(self.entry_bw2_violinplot_tab.get()), self.entry_title2_violinplot_tab.get()))
        self.button2_violinplot_tab.to_grid(7, 1, 10, 10)
        #run the window
#Scatter Plot Widgets
    #Option 1 Scatter Plots
        self.scatterplot1_frame = MyFrame(self.scatterplot_tab, 300, 300, 'white', 'solid', 1)
        self.scatterplot1_frame.to_pack('top', False, "both", 10, 10)
        #Adding X-Axis Widgets
        self.label_x1_scatterplot_tab = MyLabel(self.scatterplot1_frame, "X-Axis:")
        self.label_x1_scatterplot_tab.to_grid(0, 0, 10, 10)
        self.selected_x1_scatterplot_tab = MyStringVar(self.scatterplot1_frame)
        self.menu_x1_scatterplot_tab = MyOptionMenu(self.scatterplot1_frame, self.selected_x1_scatterplot_tab, df.columns) 
        self.menu_x1_scatterplot_tab.to_grid(0, 1, 10, 10)
        #Adding Y-Axis Widgets
        self.label_y1_scatterplot_tab = MyLabel(self.scatterplot1_frame, "Y-Axis:")
        self.label_y1_scatterplot_tab.to_grid(1, 0, 10, 10)
        self.selected_y1_scatterplot_tab = MyStringVar(self.scatterplot1_frame)
        self.menu_y1_scatterplot_tab = MyOptionMenu(self.scatterplot1_frame, self.selected_y1_scatterplot_tab, df.columns) 
        self.menu_y1_scatterplot_tab.to_grid(1, 1, 10, 10)
        #Adding Title Widgets
        self.label_title1_scatterplot_tab = MyLabel(self.scatterplot1_frame, "Title(Optional):")
        self.label_title1_scatterplot_tab.to_grid(2, 0, 10, 10)
        self.entry_title1_scatterplot_tab = MyEntry(self.scatterplot1_frame)
        self.entry_title1_scatterplot_tab.to_grid(2, 1, 10, 10)
        #Adding Button For Option 1 Frame
        self.button1_scatterplot_tab = MyButton(self.scatterplot1_frame, "Plot", lambda: plot_scatterplot1(self.visualization_frame, self.selected_x1_scatterplot_tab.get(), self.selected_y1_scatterplot_tab.get(), self.entry_title1_scatterplot_tab.get()))
        self.button1_scatterplot_tab.to_grid(3, 1, 10, 10)
    #Option 2 Scatter Plots
        self.scatterplot2_frame = MyFrame(self.scatterplot_tab, 300, 300, 'white', 'solid', 1)
        self.scatterplot2_frame.to_pack('top', False, "both", 10, 10)
        #Adding X-Axis Widgets
        self.label_x2_scatterplot_tab = MyLabel(self.scatterplot2_frame, "X-Axis:")
        self.label_x2_scatterplot_tab.to_grid(0, 0, 10, 10)
        self.selected_x2_scatterplot_tab = MyStringVar(self.scatterplot2_frame)
        self.menu_x2_scatterplot_tab = MyOptionMenu(self.scatterplot2_frame, self.selected_x2_scatterplot_tab, df.columns) 
        self.menu_x2_scatterplot_tab.to_grid(0, 1, 10, 10)
        #Adding Y-Axis Widgets
        self.label_y2_scatterplot_tab = MyLabel(self.scatterplot2_frame, "Y-Axis:")
        self.label_y2_scatterplot_tab.to_grid(1, 0, 10, 10)
        self.selected_y2_scatterplot_tab = MyStringVar(self.scatterplot2_frame)
        self.menu_y2_scatterplot_tab = MyOptionMenu(self.scatterplot2_frame, self.selected_y2_scatterplot_tab, df.columns) 
        self.menu_y2_scatterplot_tab.to_grid(1, 1, 10, 10)
        #Adding Title Widgets
        self.label_title2_scatterplot_tab = MyLabel(self.scatterplot2_frame, "Title(Optional):")
        self.label_title2_scatterplot_tab.to_grid(2, 0, 10, 10)
        self.entry_title2_scatterplot_tab = MyEntry(self.scatterplot2_frame)
        self.entry_title2_scatterplot_tab.to_grid(2, 1, 10, 10)
        #Adding Hue Widgets
        self.label_hue2_scatterplot_tab = MyLabel(self.scatterplot2_frame, "Hue:")
        self.label_hue2_scatterplot_tab.to_grid(3, 0, 10, 10)
        self.selected_hue2_scatterplot_tab = MyStringVar(self.scatterplot2_frame)
        self.menu_hue2_scatterplot_tab = MyOptionMenu(self.scatterplot2_frame, self.selected_hue2_scatterplot_tab, df.columns) 
        self.menu_hue2_scatterplot_tab.to_grid(3, 1, 10, 10)
        #Adding Palette Widgets
        palette = ["YlOrBr", "viridis"]
        self.label_palette2_scatterplot_tab = MyLabel(self.scatterplot2_frame, "Palette:")
        self.label_palette2_scatterplot_tab.to_grid(4, 0, 10, 10)
        self.selected_palette2_scatterplot_tab = MyStringVar(self.scatterplot2_frame)
        self.menu_palette2_scatterplot_tab = MyOptionMenu(self.scatterplot2_frame, self.selected_palette2_scatterplot_tab, palette) 
        self.menu_palette2_scatterplot_tab.to_grid(4, 1, 10, 10)
        #Adding Button For Option 2 Frame
        self.button2_scatterplot_tab = MyButton(self.scatterplot2_frame, "Plot", lambda: plot_scatterplot2(self.visualization_frame, self.selected_x2_scatterplot_tab.get(), self.selected_y2_scatterplot_tab.get(), self.selected_hue2_scatterplot_tab.get(), self.selected_palette2_scatterplot_tab.get(), self.entry_title2_scatterplot_tab.get()))
        self.button2_scatterplot_tab.to_grid(5, 1, 10, 10)
#Regression Plot Widgets
    #Option 1 Regression Plots
        self.regressionplot1_frame = MyFrame(self.regressionplot_tab, 300, 300, 'white', 'solid', 1)
        self.regressionplot1_frame.to_pack('top', False, "both", 10, 10)
        #Adding Regression Plot Title
        self.label_title11_regressionplot_tab = MyLabel(self.regressionplot1_frame, "Regression Plot")
        self.label_title11_regressionplot_tab.to_grid(0, 1, 10, 10)
        #Adding X-Axis Widgets
        self.label_x1_regressionplot_tab = MyLabel(self.regressionplot1_frame, "X-Axis:")
        self.label_x1_regressionplot_tab.to_grid(1, 0, 10, 10)
        self.selected_x1_regressionplot_tab = MyStringVar(self.regressionplot1_frame)
        self.menu_x1_regressionplot_tab = MyOptionMenu(self.regressionplot1_frame, self.selected_x1_regressionplot_tab, df.columns) 
        self.menu_x1_regressionplot_tab.to_grid(1, 1, 10, 10)
        #Adding Y-Axis Widgets
        self.label_y1_regressionplot_tab = MyLabel(self.regressionplot1_frame, "Y-Axis:")
        self.label_y1_regressionplot_tab.to_grid(2, 0, 10, 10)
        self.selected_y1_regressionplot_tab = MyStringVar(self.regressionplot1_frame)
        self.menu_y1_regressionplot_tab = MyOptionMenu(self.regressionplot1_frame, self.selected_y1_regressionplot_tab, df.columns) 
        self.menu_y1_regressionplot_tab.to_grid(2, 1, 10, 10)
        #Adding Title Widgets
        self.label_title1_regressionplot_tab = MyLabel(self.regressionplot1_frame, "Title(Optional):")
        self.label_title1_regressionplot_tab.to_grid(3, 0, 10, 10)
        self.entry_title1_regressionplot_tab = MyEntry(self.regressionplot1_frame)
        self.entry_title1_regressionplot_tab.to_grid(3, 1, 10, 10)
        #Adding Order Widgets
        self.label_order1_regressionplot_tab = MyLabel(self.regressionplot1_frame, "Polynomial Order:")
        self.label_order1_regressionplot_tab.to_grid(4, 0, 10, 10)
        self.entry_order1_regressionplot_tab = MyEntry(self.regressionplot1_frame)
        self.entry_order1_regressionplot_tab.to_grid(4, 1, 10, 10)
        #Adding CI Widgets
        self.label_ci1_regressionplot_tab = MyLabel(self.regressionplot1_frame, "Confidence Interval:")
        self.label_ci1_regressionplot_tab.to_grid(5, 0, 10, 10)
        self.entry_ci1_regressionplot_tab = MyEntry(self.regressionplot1_frame)
        self.entry_ci1_regressionplot_tab.to_grid(5, 1, 10, 10)
        #Adding Size Widgets
        self.label_size1_regressionplot_tab = MyLabel(self.regressionplot1_frame, "Data Point Size:")
        self.label_size1_regressionplot_tab.to_grid(6, 0, 10, 10)
        self.entry_size1_regressionplot_tab = MyEntry(self.regressionplot1_frame)
        self.entry_size1_regressionplot_tab.to_grid(6, 1, 10, 10)
        #Adding Color Widgets
        self.label_color1_regressionplot_tab = MyLabel(self.regressionplot1_frame, "Data Point Color:")
        self.label_color1_regressionplot_tab.to_grid(7, 0, 10, 10)
        self.entry_color1_regressionplot_tab = MyEntry(self.regressionplot1_frame)
        self.entry_color1_regressionplot_tab.to_grid(7, 1, 10, 10)
        #Adding Button For Option 1 Frame
        self.button1_regressionplot_tab = MyButton(self.regressionplot1_frame, "Plot", lambda: plot_regressionplot1(self.visualization_frame, self.selected_x1_regressionplot_tab.get(), self.selected_y1_regressionplot_tab.get(), float(self.entry_order1_regressionplot_tab.get()), float(self.entry_ci1_regressionplot_tab.get()), float(self.entry_size1_regressionplot_tab.get()), self.entry_color1_regressionplot_tab.get(), self.entry_title1_regressionplot_tab.get()))
        self.button1_regressionplot_tab.to_grid(8, 1, 10, 10)
#Bar Plot Widgets
        self.barplot1_frame = MyFrame(self.barplot_tab, 300, 300, 'white', 'solid', 1)
        self.barplot1_frame.to_pack('top', False, "both", 10, 10)
        #Adding Bar Plot Label
        self.label_title11_barplot_tab = MyLabel(self.barplot1_frame, "Bar Plot")
        self.label_title11_barplot_tab.to_grid(0, 1, 10, 10)
        #Adding X-Axis Widgets
        self.label_x1_barplot_tab = MyLabel(self.barplot1_frame, "X-Axis:")
        self.label_x1_barplot_tab.to_grid(1, 0, 10, 10)
        self.selected_x1_barplot_tab = MyStringVar(self.barplot1_frame)
        self.menu_x1_barplot_tab = MyOptionMenu(self.barplot1_frame, self.selected_x1_barplot_tab, df.columns) 
        self.menu_x1_barplot_tab.to_grid(1, 1, 10, 10)
        #Adding Order Widgets
        self.label_order1_barplot_tab = MyLabel(self.barplot1_frame, "Order By:")
        self.label_order1_barplot_tab.to_grid(2, 0, 10, 10)
        self.selected_order1_barplot_tab = MyStringVar(self.barplot1_frame)
        self.menu_order1_barplot_tab = MyOptionMenu(self.barplot1_frame, self.selected_order1_barplot_tab, df.columns) 
        self.menu_order1_barplot_tab.to_grid(2, 1, 10, 10)
        #Adding Button For Option 1 Frame
        self.button1_barplot_tab = MyButton(self.barplot1_frame, "Plot", lambda: plot_barplot1(self.visualization_frame, self.selected_x1_barplot_tab.get(), self.selected_order1_barplot_tab.get()))
        self.button1_barplot_tab.to_grid(3, 1, 10, 10)


class MyCanvas(tk.Canvas):
    def __init__(self, parent, width, height):
        super().__init__(parent, width=width, height=height)
    def to_pack(self, side, expand, fill, padx, pady):
        self.pack(side=side, expand=expand, fill=fill, padx=padx, pady=pady)
    def add_window(self, coords, window, anchor):
        self.create_window(coords, window=window, anchor=anchor)
    def configurate(self, canvas):
        self.configure(scrollregion=canvas)

class MyScrollbar(tk.Scrollbar):
    def __init__(self, parent, orient, command):
        super().__init__(parent, orient=orient, command=command) 
    def to_pack(self, side, expand, fill, padx, pady):
        self.pack(side=side, expand=expand, fill=fill, padx=padx, pady=pady)

class MyNotebook(ttk.Notebook):
    def __init__(self, parent, width, height):
        super().__init__(parent, width=width, height=height)
    def to_pack(self, side, expand, fill, padx, pady):
        self.pack(side=side, expand=expand, fill=fill, padx=padx, pady=pady)
    def add_tab(self, tab, text):
        self.add(tab, text=text)
    def update(self):
        self.update_idletasks()

class MyFrame(tk.Frame):
    def __init__(self, parent, width, height, bg, relief, borderwidth):
        super().__init__(parent, width=width, height=height, bg=bg, relief=relief, borderwidth=borderwidth)
    def to_grid(self, row, column, padx, pady):
        self.grid(row=row, column=column, padx=padx, pady=pady)
    def to_pack(self, side, expand, fill, padx, pady):
        self.pack(side=side, expand=expand, fill=fill, padx=padx, pady=pady)

class MyLabel(tk.Label):
    def __init__(self, parent, text):
        super().__init__(parent, text=text)
    def to_grid(self, row, column, padx, pady):
        self.grid(row=row, column=column, padx=padx, pady=pady)
    
class MyButton(tk.Button):
    def __init__(self, parent, text, command):
        super().__init__(parent, text=text, command=command)
    def to_grid(self, row, column, padx, pady):
        self.grid(row=row, column=column, padx=padx, pady=pady)
    
class MyOptionMenu(tk.OptionMenu):
    def __init__(self, parent, selected_value, columns):
        super().__init__(parent, selected_value, *columns)
    def to_grid(self, row, column, padx, pady):
        self.grid(row=row, column=column, padx=padx, pady=pady)
    
class MyStringVar(tk.StringVar):
    def __init__(self, parent):
        super().__init__(parent)
        self.set(None)

class MyEntry(tk.Entry):
    def __init__(self, parent):
        super().__init__(parent)
    def to_grid(self, row, column, padx, pady):
        self.grid(row=row, column=column, padx=padx, pady=pady)
        