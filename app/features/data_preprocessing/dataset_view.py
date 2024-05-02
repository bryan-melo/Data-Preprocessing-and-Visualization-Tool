import pandas as pd
import numpy as np

from tkinter import *
from tkinter import ttk


def populate_treeview(tree):
    df = return_df()    # import dataset
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"

    for col in df.columns:
        tree.column(col, anchor=CENTER, width=2)
        tree.heading(col, text=col, anchor='w')

    for row in df.to_numpy().tolist():
        tree.insert('', 'end', values=row)

        
def return_df():
    # Sample DataFrame
    data = {
        'ID': np.random.randint(1, 100, size=1000),
        'Name': ['Name_' + str(i) for i in range(1000)],
        'Date': pd.date_range(start='1/1/2022', periods=1000),
        'Value': np.random.randint(1, 1000, size=1000)
    }

    df = pd.DataFrame(data)
    df.reset_index(inplace=True)
    
    return df
    