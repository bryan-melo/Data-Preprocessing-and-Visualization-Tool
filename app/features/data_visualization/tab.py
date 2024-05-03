import tkinter as tk
from tkinter import *
from tkinter import ttk
import seaborn as sns
from matplotlib.figure import Figure
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# #Read The Data And Prepare the Columns List
df = pd.read_csv("https://raw.githubusercontent.com/csbfx/advpy122-data/master/contigs.csv")

#Set the columns
columns = df.columns.to_list()

#Function For Relational Plot
def plot_relational():
    # settings = {"x":selected_x_value.get(), "y":selected_y_value.get(), "x_lower_bound":x_lower_entry.get(), "x_upper_bound":x_higher_entry.get(), "y_lower_bound":y_lower_entry.get(), "y_upper_bound":y_higher_entry.get(), "hue":selected_hue_column.get(), "palette":selected_hue_palette.get(), "size":selected_size_column.get(), "title":title_entry.get(), "alpha":alpha_entry.get(), "s":data_point_size_entry.get()}
    # settings_to_be_used = {}
    # for key, value in settings:
        # if(value != None):
            # settings_to_be_used[key] = value
    # plot(setting for setting in settings_to_be_used)    
    # hue_column = selected_hue_column.get()
    # hue = hue_column if hue_column else None
    sns_plot = sns.relplot(
        data = df,
        x = selected_x_value.get(),
        y = selected_y_value.get(),
        # palette = selected_hue_palette.get()
    )
    fig = sns_plot.figure
    canvas = FigureCanvasTkAgg(fig, master=visualization_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# def plot(x=None, y=None, ):

#Window set up
root = tk.Tk()
root.geometry = '1200x1200'
root.title("Plot Inputs")
root.config(bg="navy")

# Create a canvas in the root
canvas = tk.Canvas(root, width=200, height=800)
canvas.pack(side='left', fill='both', expand=True, padx=10, pady=10)

# Add a vertical scrollbar in the root 
y_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
y_scrollbar.pack(side='left', fill='both', padx=5, pady=10)

#Create Notebook In The Canvas
main_tab = ttk.Notebook(canvas, width=450, height=800)
rel_plot_tab = tk.Frame(main_tab, width=200, height=800, bg='lightblue', relief='solid', borderwidth=1)
cat_plot_tab = tk.Frame(main_tab, width=200, height=800, bg='lightblue', relief='solid', borderwidth=1)
main_tab.add(rel_plot_tab, text='Relational Plot')
main_tab.add(cat_plot_tab, text='Boxplot')
main_tab.pack(expand=True, fill='both', padx=5, pady=5)

# Create a frame inside the canvas to hold the widgets
canvas.create_window((0, 0), window=main_tab, anchor=tk.NW)

# Update main tab 
main_tab.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))


#Visualization Frame
visualization_frame = tk.Frame(root, height=500, width=500, bg="lightblue", relief='solid', borderwidth=1)
visualization_frame.pack(side='left', fill='both', expand=True, pady=10, padx=10)

# Axes Selection Frame
axes_selection_frame = tk.Frame(rel_plot_tab, width=750, height=300, bg='white', relief='solid', borderwidth=1)
axes_selection_frame.pack(side='top', fill='both', padx=10, pady=10)

#Labels For Axes Selection
x_label = tk.Label(axes_selection_frame, text="x-axis:")
x_label.grid(column=0, row=0, padx=10, pady=10)
y_label = tk.Label(axes_selection_frame, text="y-axis:")
y_label.grid(column=0, row=1, padx=10, pady=10)

#Option Column Selection X-axis
selected_x_value = tk.StringVar(axes_selection_frame)
selected_x_value.set(None)  # Set default value
option_menu = tk.OptionMenu(axes_selection_frame, selected_x_value, *columns)
option_menu.grid(column=1, row=0, padx=10, pady=10)

#Option Column Selection Y-axis
selected_y_value = tk.StringVar(axes_selection_frame)
selected_y_value.set(None)  # Set default value
option_menu = tk.OptionMenu(axes_selection_frame, selected_y_value, *columns)
option_menu.grid(column=1, row=1, padx=10, pady=10)

# Limit Frame
limit_frame = tk.Frame(rel_plot_tab, width=750, height=300, bg='white', relief='solid', borderwidth=1)
limit_frame.pack(side='top', fill='both', padx=10)

#Labels For The Lower/Upper Bounds
x_lower_label = tk.Label(limit_frame, text="x-axis lower bound:")
x_lower_label.grid(column=0, row=0, padx=10, pady=10)
x_higher_label = tk.Label(limit_frame, text="x-axis upper bound:")
x_higher_label.grid(column=0, row=1, padx=10, pady=10)
y_lower_label = tk.Label(limit_frame, text="y-axis lower bound:")
y_lower_label.grid(column=0, row=2, padx=10, pady=10)
y_higher_label = tk.Label(limit_frame, text="y-axis upper bound:")
y_higher_label.grid(column=0, row=3, padx=10, pady=10)

#Entries For The Lower/Upper Bounds
x_lower_entry = tk.Entry(limit_frame)
x_lower_entry.grid(column=1, row=0, padx=10, pady=10)
x_higher_entry = tk.Entry(limit_frame)
x_higher_entry.grid(column=1, row=1, padx=10, pady=10)
y_lower_entry = tk.Entry(limit_frame)
y_lower_entry.grid(column=1, row=2, padx=10, pady=10)
y_higher_entry = tk.Entry(limit_frame)
y_higher_entry.grid(column=1, row=3, padx=10, pady=10)

#Hue Frame
hue_frame = tk.Frame(rel_plot_tab, width=750, height=300, bg='white', relief='solid', borderwidth=1)
hue_frame.pack(side='top', fill='both', padx=10, pady=10)

#Hue Label
hue_label = tk.Label(hue_frame, text="Hue Column:")
hue_label.grid(column=0, row=0, padx=10, pady=10)

#Hue Option
selected_hue_column = tk.StringVar(hue_frame)
selected_hue_column.set(None)  # Set default value
hue_menu = tk.OptionMenu(hue_frame, selected_hue_column, *columns)
hue_menu.grid(column=1, row=0, padx=10, pady=10)

#Hue Palette
hue_palette_label = tk.Label(hue_frame, text="Hue Color:")
hue_palette_label.grid(column=0, row=1, padx=10, pady=10)

#Hue Palette Option
hue_palettes = ["YlOrBr", "viridis"]
selected_hue_palette = tk.StringVar(hue_frame)
selected_hue_palette.set(None)  # Set default value
hue_color_menu = tk.OptionMenu(hue_frame, selected_hue_palette, *hue_palettes)
hue_color_menu.grid(column=1, row=1, padx=10, pady=10)

#Size Frame
size_frame = tk.Frame(rel_plot_tab, width=750, height=300, bg='white', relief='solid', borderwidth=1)
size_frame.pack(side='top', fill='both', padx=10, pady=10)

size_label = tk.Label(size_frame, text="Size Column:")
size_label.grid(column=0, row=0, padx=10, pady=10)

selected_size_column = tk.StringVar(size_frame)
selected_size_column.set(None)  # Set default value
size_menu = tk.OptionMenu(size_frame, selected_size_column, *columns)
size_menu.grid(column=1, row=0, padx=10, pady=10)

#Default Size Range
sizes = (2,150)

#Title Frame
title_frame = tk.Frame(rel_plot_tab, width=750, height=300, bg='white', relief='solid', borderwidth=1)
title_frame.pack(side='top', fill='both', padx=10, pady=10)

title_label = tk.Label(title_frame, text="Title Name:")
title_label.grid(column=0, row=0, padx=10, pady=10)

title_entry = tk.Entry(title_frame, width=50)
title_entry.grid(column=1, row=0, padx=10, pady=10)

#Default Title Y-Axis Pad 
pad = 20

#Alpha & Size Frame
solve_dense_frame = tk.Frame(rel_plot_tab, width=750, height=300, bg='white', relief='solid', borderwidth=1)
solve_dense_frame.pack(side='top', fill='both', padx=10, pady=10)

alpha_label = tk.Label(solve_dense_frame, text="Alpha Value:")
alpha_label.grid(column=0, row=0, padx=10, pady=10)

alpha_entry = tk.Entry(solve_dense_frame)
alpha_entry.grid(column=1, row=0, padx=10, pady=10)

data_point_size_label = tk.Label(solve_dense_frame, text="Data Point Size:")
data_point_size_label.grid(column=0, row=1, padx=10, pady=10)

data_point_size_entry = tk.Entry(solve_dense_frame)
data_point_size_entry.grid(column=1, row=1, padx=10, pady=10)

#Plot button
plot_button = tk.Button(rel_plot_tab, text="Plot", command=plot_relational)
plot_button.pack(side='top', padx=10, pady=10)

#---------------------------------------------------------------------------------------------------------------------#
#Cat Plot Frame

axes_cat_frame = tk.Frame(cat_plot_tab, width=750, height=300, bg='white', relief='solid', borderwidth=1)
axes_cat_frame.pack(side='top', fill='both', padx=10, pady=10)

x_label_axes_cat = tk.Label(axes_cat_frame, text="x-axis:")
x_label_axes_cat.grid(column=0, row=0, padx=10, pady=10)
y_label_axes_cat = tk.Label(axes_cat_frame, text="y-axis:")
y_label_axes_cat.grid(column=0, row=1, padx=10, pady=10)

#Axes Selection
selected_x_value_axes_cat = tk.StringVar(axes_cat_frame)
selected_x_value_axes_cat.set(None)  # Set default value
x_option_menu = tk.OptionMenu(axes_cat_frame, selected_x_value_axes_cat, *columns)
x_option_menu.grid(column=1, row=0, padx=10, pady=10)

selected_y_value_axes_cat = tk.StringVar(axes_cat_frame)
selected_y_value_axes_cat.set(None)  # Set default value
y_option_menu = tk.OptionMenu(axes_cat_frame, selected_y_value_axes_cat, *columns)
y_option_menu.grid(column=1, row=1, padx=10, pady=10)

order_frame = tk.Frame(cat_plot_tab, width=750, height=300, bg='white', relief='solid', borderwidth=1)
order_frame.pack(side='top', fill='both', padx=10, pady=10)

selected_order_label = tk.StringVar(order_frame)
selected_order_label.set(None)  # Set default value
order_option_menu = tk.OptionMenu(order_frame, selected_order_label, *columns)
order_option_menu.grid(column=1, row=0, padx=10, pady=10)


root.mainloop()