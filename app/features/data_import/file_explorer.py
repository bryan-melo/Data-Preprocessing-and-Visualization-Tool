from pathlib import Path

project_directory = Path(r'../cs122/app/datasets')


def populate_file_explorer_treeview(file_explorer_treeview):
    # Delete all existing items
    file_explorer_treeview.delete(*file_explorer_treeview.get_children())

    # Insert the root item
    root_item = file_explorer_treeview.insert("", "end", open=True)

    # Recursively insert folders and files from the project directory
    insert_folder(file_explorer_treeview, root_item, project_directory)
    
    return file_explorer_treeview



def insert_folder(treeview, parent, path):
    # Insert the current folder
    folder_item = treeview.insert(parent, "end", text=path.name, open=True)

    # Get subfolders and files and sort them
    try:
        subfolders = sorted([sub_path for sub_path in path.iterdir() if sub_path.is_dir()])
        files = sorted([sub_path for sub_path in path.iterdir() if sub_path.is_file()])
        
        for sub_path in subfolders:
            insert_folder(treeview, folder_item, sub_path)
            
        for sub_path in files:
            treeview.insert(folder_item, "end", text=sub_path.name)
    except PermissionError:
        pass


def on_select(treeview, data_select):
    selected_item = treeview.focus()
    if selected_item:
        item_text = treeview.item(selected_item, "text")
        parent_item = treeview.parent(selected_item)
        path = Path(project_directory, item_text)
        data_select.file_name = str(path)
        data_select.update_df(data_select.df)
        print("Selected file path:", path)
