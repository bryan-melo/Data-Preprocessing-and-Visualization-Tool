from tkinter import CENTER

def populate_treeview(tree, df):
    # Clear existing items in the tree view
    tree.delete(*tree.get_children())
    
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"

    for col in df.columns:
        tree.column(col, anchor=CENTER)
        tree.heading(col, text=col, anchor='w')

    for row in df.to_numpy().tolist():
        tree.insert('', 'end', values=row)
        
    return tree
