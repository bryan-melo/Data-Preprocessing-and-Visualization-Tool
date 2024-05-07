import pandas as pd

from features.data_preprocessing.dataset_view import populate_treeview
from features.data_preprocessing.dataset_overview import retrieve_info 


class DataSelect:
    def __init__(self, file_name=None, tree_view=None, df_info_canvas=None, df_info=None):
        self._file_name = file_name
        self._df = pd.read_csv(file_name)  # Assuming the file is a CSV, adjust as needed
        self._tree_view = tree_view
        self._df_info_canvas = df_info_canvas
        self._df_info = df_info
        self._undo_df = None

    @property
    def file_name(self):
        return self._file_name
    
    @file_name.setter
    def file_name(self, file_name):
        self._file_name = file_name
        self._df = pd.read_csv(file_name)

    @property
    def df(self):
        return self._df

    @df.setter
    def df(self, new_df):
        self._undo_df = self._df.copy()  # Store a copy of the current DataFrame
        self._df = new_df

    @property
    def tree_view(self):
        return self._tree_view

    @tree_view.setter
    def tree_view(self, value):
        self._tree_view = value

    @property
    def df_info_canvas(self):
        return self._df_info_canvas

    @df_info_canvas.setter
    def df_info_canvas(self, value):
        self._df_info_canvas = value

    @property
    def df_info(self):
        return self._df_info

    @df_info.setter
    def df_info(self, value):
        self._df_info = value

    def update_df(self, new_df):
        self.df = new_df
        populate_treeview(self.tree_view, self.df)
        info_text = retrieve_info(self.df)
        overview_text = "\n".join(info_text[1:-3])
        self.change_df_info_text(overview_text, self.df_info_canvas, self.df_info)

    def change_df_info_text(self, new_text, canvas, text):
        canvas.itemconfig(text, text=new_text)

    def undo_changes(self):
        if self._undo_df is not None:
            self._df = self._undo_df.copy()  # Restore the previous DataFrame state
            self.update_df(self.df)
            self._undo_df = None  # Clear the undo DataFrame after using it


