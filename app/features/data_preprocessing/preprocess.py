import tkinter as tk
import pandas as pd
import pandastable as pt
import polars as pl

def search():
        pandas_dataset_df = pd.read_csv(url_entry.get())
        lazy_frame_dataset = pl.LazyFrame(pandas_dataset_df) #convert pandas df to LazyFrame to make querying memory-efficient
        #row_restraint = row_entry.get()
        column_restraint = str(column_entry.get())
        polars_df_query = (
            lazy_frame_dataset
            .collect()
            .select(
                pl.col([column_restraint])
            )
        )
        searched_pandas_df = polars_df_query.to_pandas()
        edited_pandas_table = pt.Table(middle_frame, dataframe=searched_pandas_df, showtoolbar=True, showstatusbar=True)
        edited_pandas_table.show()

def show_data_url():
    pandas_dataset_df = pd.read_csv(url_entry.get())
    pandas_table = pt.Table(right_frame, dataframe=pandas_dataset_df, showtoolbar=True, showstatusbar=True)
    pandas_table.show()

#Window set up
root = tk.Tk()
root.geometry = '1200x1200'
root.title("Data Preprocessing Page")
root.config(bg="navy")

#Left Frame
left_frame = tk.Frame(root, width=325, height=300, bg='lightblue', relief='solid', borderwidth=2)
left_frame.pack(side='left', fill='y', expand=True, padx=5, pady=5)

#Middle Frame
middle_frame = tk.Frame(root, width=450, height=300, bg='lightblue', relief='solid', borderwidth=2)
middle_frame.pack(side='left', fill='y', expand=True, padx=0, pady=5)

#Right Frame
right_frame = tk.Frame(root, width=450, height=300, bg='lightblue', relief='solid', borderwidth=2)
right_frame.pack(side='right', fill='both', expand=True, padx=5, pady=5)

#Data Enter URL Frame
data_url_frame = tk.Frame(left_frame, relief="solid", width=300, height=300, borderwidth=1, bg="white")
data_url_frame.pack(side=tk.TOP, anchor='n', fill='x', pady=10, padx=10, expand=True)

label1 = tk.Label(data_url_frame, text="Enter data URL:", bg='lightgrey')
label1.grid(row=0, column=1, padx=5, pady=10)

url_entry = tk.Entry(data_url_frame, width=30)
url_entry.grid(row=0, column=2, padx=5, pady=10)

show_data_button = tk.Button(data_url_frame, text='Show Data', command=show_data_url)
show_data_button.grid(row=1, column=1, padx=5, pady=10)

#Data Search Configuration Frame
data_search_configure_frame = tk.Frame(left_frame, bg="white", width=300, height=600, relief='solid', borderwidth=1)
data_search_configure_frame.pack(side=tk.TOP, anchor='s', fill='x', padx=10, pady=10, expand=True)

#Advanced Search Widgets
row_label = tk.Label(data_search_configure_frame, text="Row Condition:", bg='lightgrey')
row_label.grid(row=0, column=0, padx=5, pady=5)

row_entry = tk.Entry(data_search_configure_frame, width=30)
row_entry.grid(row=0, column=1, padx=5, pady=5)

column_label = tk.Label(data_search_configure_frame, text="Column Condition:", bg='lightgrey')
column_label.grid(row=1, column=0, padx=5, pady=5)

column_entry = tk.Entry(data_search_configure_frame, width=30)
column_entry.grid(row=1, column=1, padx=5, pady=5)

search_button = tk.Button(data_search_configure_frame, text="Search", command=search)
search_button.grid(row=2, column=1, padx=5, pady=5)



#search particular records
#drop columns
#edit/update particular records
#aggregate functions mean, std, etc.

root.mainloop()