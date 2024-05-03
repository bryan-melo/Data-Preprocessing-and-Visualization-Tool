import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

root = tk.Tk()
root.geometry("1600x900")  # width x height
root.pack_propagate(False)  # keep original window size
root.resizable(None, None)    # disable resizing

# Dataframe view
frame1 = tk.LabelFrame(root, text="Data")
frame1.place(x=10, y=10, height=500, width=780)
1
# Plot view
frame2 = tk.LabelFrame(root, text="Plot")
frame2.place(x=810, y=10, height=500, width=780)

# Treeview widget
tree = ttk.Treeview(frame1)
tree.place(relheight=1, relwidth=1)

tree_scroll_y = tk.Scrollbar(frame1, orient="vertical", command=tree.yview)
tree_scroll_x = tk.Scrollbar(frame1, orient="horizontal", command=tree.xview)
tree.configure(xscrollcommand=tree_scroll_x.set, yscrollcommand=tree_scroll_y.set)
tree_scroll_x.pack(side="bottom", fill="x")
tree_scroll_y.pack(side="right", fill="y")

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

df.reset_index(inplace=True)

tree["columns"] = list(df.columns)
tree["show"] = "headings"

for col in df.columns:
    tree.heading(col, text=col, anchor='w')

for row in df.to_numpy().tolist():
    tree.insert('', 'end', values=row)

root.mainloop()
