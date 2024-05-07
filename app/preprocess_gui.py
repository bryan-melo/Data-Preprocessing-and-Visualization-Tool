# Library imports
import tkinter as tk

from tkinter import ttk
from pathlib import Path

# Module imports
from features.data_preprocessing.dataset_view import populate_treeview
from features.data_preprocessing.dataset_overview import retrieve_info 
from features.data_import.file_explorer import populate_file_explorer_treeview
from features.data_preprocessing.dataset_operations import create_tabs
from features.data_import.dataset_selection import DataSelect
from features.data_import.file_explorer import on_select
from features.data_export.dataframe_export import dataframe_to_csv_export


# Dataset initializer
data_select = DataSelect(file_name='../cs122/app/datasets/AppleStore.csv') 


class PreprocessPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        ## Create border canvas
        canvas = tk.Canvas(
            self,
            bg = "#FFFFFF",
            height = 800,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        canvas.place(x = 0, y = 0)
        
        # Header
        canvas.create_rectangle(
            0.0,
            0.0,
            1280.0,
            55.0,
            fill="#141414",
            outline="")
        
        preprocess_button = tk.Button(
            self,
            text='Preprocess',
            fg='blue',
        )
        
        preprocess_button.place(
            x=250.0,
            y=0.0,
            width=150.0,
            height=55.0
        )

        visualize_button = tk.Button(
            self,
            text='Visualize',
            #command=self.visualize_data
        )
        
        visualize_button.place(
            x=400.0,
            y=0.0,
            width=150.0,
            height=55.0
        )
        
        # Explorer view 
        canvas.create_text(
            70.0,
            20.0,
            anchor="nw",
            text="FILE EXPLORER",
            fill="#BBBBBB",
            font=("KaiseiTokumin Regular", 14)
        )
        
        file_explorer_canvas = tk.Canvas(
            self,
            width=250,
            height=745,
            bg="#282828"
        )
        file_explorer_canvas.place(x=0, y=55)
        
        file_explorer_treeview = ttk.Treeview(file_explorer_canvas)
        file_explorer_treeview.place(x=0, y=0, width=250, height=745)
        
        populate_file_explorer_treeview(file_explorer_treeview)
                        
        # Export button
        export_button = tk.Button(
            self,
            text='Export',
            command=lambda: dataframe_to_csv_export(data_select, file_explorer_treeview),
            fg='green'
        )
        
        export_button.place(
            x=1130.0,
            y=0.0,
            width=150.0,
            height=55.0,
        )
        
        # Load button
        load_button = ttk.Button(
            self,
            text='Load',
            command=lambda: on_select(file_explorer_treeview, data_select),
        )
        
        load_button.place(
            x=0.0,
            y=770.0,
            width=250.0,
            height=35.0,
        )
        
        # Dataset canvas
        preprocess_canvas = tk.Canvas(
            self, 
            width=1025, 
            height=740, 
            bg="#282828"
        )
        preprocess_canvas.place(x=250, y=55)

        ## Dataset View
        preprocess_canvas.create_rectangle(
            25,    # x0
            50,    # y0
            1000,    # x1
            400,    # y1
            fill="#FFFFFF",
        )
        
        # Undo button
        undo_button = ttk.Button(
            preprocess_canvas,
            text='Undo',
            command=lambda: data_select.undo_changes(),
        )
        
        undo_button.place(
            x=555.0,
            y=435.0,
        )

        preprocess_canvas.create_text(
            95,
            30,
            text='DATASET VIEW:'
        )

        # Add tree view to Dataset View
        view_tree = ttk.Treeview(preprocess_canvas)
        view_tree.place(x=25, y=50, width=976, height=351)

        # Apply the custom style to the treeview
        view_tree.configure(style="Custom.Treeview")

        # Apply the custom style to the scrollbars
        view_tree_scroll_y = ttk.Scrollbar(preprocess_canvas, orient="vertical", command=view_tree.yview, style="Vertical.TScrollbar")
        view_tree_scroll_x = ttk.Scrollbar(preprocess_canvas, orient="horizontal", command=view_tree.xview, style="Horizontal.TScrollbar")

        view_tree_scroll_x.place(x=25, y=401, width=976)
        view_tree_scroll_y.place(x=1001, y=50, height=351)

        view_tree.configure(yscrollcommand=view_tree_scroll_y.set, xscrollcommand=view_tree_scroll_x.set)

        # Populate tree_view
        tree = populate_treeview(view_tree, data_select.df)
        
        # Add tree_view to data_select
        data_select.tree_view = tree

        ## Dataset overview
        preprocess_canvas.create_text(
            770,
            450,
            text='DATASET OVERVIEW:'
        )
          
        df_info_canvas = overview_canvas = tk.Canvas(
            self,
            bg='#282828',
            width=310,
            height=231,
        )
        overview_canvas.place(x=935, y=525)
        
        # Create scrollbars for overview_canvas
        overview_scroll_y = ttk.Scrollbar(self, orient="vertical", command=overview_canvas.yview)
        overview_scroll_x = ttk.Scrollbar(self, orient="horizontal", command=overview_canvas.xview)

        # Place the scrollbars
        overview_scroll_x.place(x=935, y=762, width=316)
        overview_scroll_y.place(x=1250, y=525, height=239)

        # Configure the canvas to use the scrollbars
        overview_canvas.configure(yscrollcommand=overview_scroll_y.set, xscrollcommand=overview_scroll_x.set)
        
        # Add canvas to data_select
        data_select.df_info_canvas = df_info_canvas
        
        # Retrieve dataset .info 
        info_text = retrieve_info(data_select.df)
        overview_text = "\n".join(info_text[1:-3])
        
        df_info = overview_canvas.create_text(
            10,
            10,
            anchor='nw',
            text=overview_text,
            fill='white',
            font=("KaiseiTokumin Regular", 14),
            justify='left'
        )
        
        # Add df_info to data_select
        data_select.df_info = df_info
        
        # Dataset operations
        preprocess_canvas.create_text(
            115,
            450,
            text='DATASET OPERATIONS:'
        )
        
        operations_canvas = tk.Canvas(
            self,
            bg = "#282828",
            height =251,
            width = 626,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        operations_canvas.place(x=275, y=525)
        
        # Create tabs for dataset operations
        create_tabs(operations_canvas, data_select)


    def tree_view_style():
        # Create a custom style
        style = ttk.Style()

        # Configure the custom style
        style.configure("Custom.Treeview", background="#282828", foreground="white", fieldbackground="#282828")
        style.map("Custom.Treeview", background=[("selected", "#558CC1")])  # Change selected item background color
        style.configure("Custom.Treeview.Heading", foreground="white")  # Change column text color

        style.configure("Vertical.TScrollbar", troughcolor="#282828", background="#1f1f1f", arrowcolor="white")
        style.map("Vertical.TScrollbar", background=[("active", "#1f1f1f")])

        style.configure("Horizontal.TScrollbar", troughcolor="#282828", background="#1f1f1f", arrowcolor="white")
        style.map("Horizontal.TScrollbar", background=[("active", "#1f1f1f")])
        
