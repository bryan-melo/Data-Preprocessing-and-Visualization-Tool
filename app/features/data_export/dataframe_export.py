import pandas as pd

from pathlib import Path
from features.data_import.file_explorer import populate_file_explorer_treeview


EXPORT_PATH = Path(r'../cs122/app/datasets/')

def dataframe_to_csv_export(data_select, file_explorer_treeview):
    file_name = data_select.file_name
    file_name = file_name.split('/')
    i = 1
    while True:
        export_file_path = EXPORT_PATH / f'{file_name[-1]}({i}).csv'
        if not export_file_path.exists():
            break
        i += 1
        
    df = data_select.df
    df.to_csv(export_file_path)
    populate_file_explorer_treeview(file_explorer_treeview)
    