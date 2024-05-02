import tkinter as tk
from tkinter import ttk
from pathlib import Path

project_directory = Path(r'/Users/bryanmelo/Documents/GitHub/cs122')


def populate_file_explorer_treeview(file_explorer_canvas):
    # Create a treeview widget
    file_explorer_treeview = ttk.Treeview(file_explorer_canvas)
    file_explorer_treeview.place(x=0, y=0, width=250, height=745)

    # Insert the root item
    root_item = file_explorer_treeview.insert("", "end", text=project_directory.name, open=True)

    # Recursively insert folders and files from the project directory
    insert_folder(file_explorer_treeview, root_item, project_directory)


def insert_folder(treeview, parent, path):
    # Insert the current folder
    folder_item = treeview.insert(parent, "end", text=path.name, open=False)

    # Iterate over subfolders and files
    try:
        for sub_path in path.iterdir():
            if sub_path.is_dir():
                # Recursively insert subfolders
                insert_folder(treeview, folder_item, sub_path)
            else:
                # Insert files
                treeview.insert(folder_item, "end", text=sub_path.name)
    except PermissionError:
        # Handle permission errors by skipping the folder
        pass