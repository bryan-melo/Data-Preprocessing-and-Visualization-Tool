import pandas as pd
import tkinter as tk

from tkinter import ttk


def create_tabs(operations_canvas, data_select):
    # Create outer tab container
    operations_tab = ttk.Notebook(operations_canvas, width=640, height=225)
    operations_tab.place(x=-30, y=-10)
    
    # Create frames for tabs
    cleaning_frame = tk.Frame(operations_tab, bg='#282828')
    sorting_frame = tk.Frame(operations_tab, bg='#282828')
    melt_frame = tk.Frame(operations_tab, bg='#282828')
    aggregate_frame = tk.Frame(operations_tab, bg='#282828')
    pivot_frame = tk.Frame(operations_tab, bg='#282828')
    
    # Add tabs to container
    operations_tab.add(cleaning_frame, text='Clean', sticky="nsew")
    operations_tab.add(sorting_frame, text='Sort', sticky="nsew")
    operations_tab.add(melt_frame, text='Melt', sticky="nsew")
    operations_tab.add(pivot_frame, text='Pivot', sticky="nsew")
    operations_tab.add(aggregate_frame, text='Aggregate', sticky="nsew")

    
    # Add labels & inputs for outer tab frames
    sort_data_labels(sorting_frame, data_select)
    melt_labels(melt_frame, data_select)
    pivot_labels(pivot_frame, data_select)
    aggregate_labels(aggregate_frame, data_select)
    
    # Create inner tab container
    clean_tab = ttk.Notebook(cleaning_frame, width=500, height=201)
    clean_tab.place(x=-34, y=-10)
    
    # Create frames inner tab container
    missing_values_frame = tk.Frame(clean_tab, bg='#282828')
    duplicate_data_frame = tk.Frame(clean_tab, bg='#282828') 
    data_type_frame = tk.Frame(clean_tab, bg='#282828') 
    text_cleaning_frame = tk.Frame(clean_tab, bg='#282828') 
    column_operations_frame = tk.Frame(clean_tab, bg='#282828')
    
    # Add tabs to inner container
    clean_tab.add(missing_values_frame, text='Missing Values', sticky='nsew')
    clean_tab.add(duplicate_data_frame, text='Duplicate Values', sticky='nsew')
    clean_tab.add(data_type_frame, text='Type Conversion', sticky='nsew')
    clean_tab.add(text_cleaning_frame, text='Reformat Text', sticky='nsew')
    clean_tab.add(column_operations_frame, text='Columns Operations', sticky='nsew')
    
    # Add labels & inputs to inner clean tab frames 
    missing_values_labels(missing_values_frame, data_select)
    duplicate_data_labels(duplicate_data_frame, data_select)
    data_type_labels(data_type_frame, data_select)
    text_cleaning_labels(text_cleaning_frame, data_select)
    column_operations_labels(column_operations_frame, data_select)
        

# Outer labels 
def sort_data_labels(sorting_frame, data_select):
    # sort_by label & input
    sort_by_label = tk.Label(sorting_frame, text='Sort by column(s) : {str, list}' , bg='#282828', fg='white')
    sort_by_label.place(x=10, y=30)
    
    sort_by_input = ttk.Entry(sorting_frame, width=15)
    sort_by_input.place(x=210, y=30)
    
    # ascending label & input
    ascending_label = tk.Label(sorting_frame, text='ascending : {True, False} ', bg='#282828', fg='white')
    ascending_label.place(x=10, y=80)
    
    ascending_input = ttk.Entry(sorting_frame, width=10)
    ascending_input.place(x=190, y=80)
    
    # kind label & input
    kind_label = tk.Label(sorting_frame, text="kind : {'quicksort', 'mergesort', 'heapsort', 'stable'} ", bg='#282828', fg='white')
    kind_label.place(x=10, y=130)
    
    kind_input = ttk.Entry(sorting_frame, width=15)
    kind_input.place(x=350, y=130)
    
    # submit button
    sort_data_submit_button = ttk.Button(sorting_frame, text='Submit', command=lambda: submit_values({'sort_by': sort_by_input.get(), 'ascending': ascending_input.get(), 'kind': kind_input.get()}, sort_data, data_select))
    sort_data_submit_button.place(x=525, y=200)
    

def melt_labels(melt_frame, data_select):
    # id_vars label & input
    id_vars_label = tk.Label(melt_frame, text='Columns to use as identifier variables : {scalar, tuple, list} ', bg='#282828', fg='white')
    id_vars_label.place(x=10, y=30)
    
    id_vars_input = ttk.Entry(melt_frame, width=20)
    id_vars_input.place(x=390, y=30)
    
    # value_vars label & input
    value_vars_label = tk.Label(melt_frame, text='Column(s) to unpivot : {scalar, tuple, list} ', bg='#282828', fg='white')
    value_vars_label.place(x=10, y=80)
    
    value_vars_input = ttk.Entry(melt_frame, width=20)
    value_vars_input.place(x=290, y=80)
    
    # var_name label & input
    var_name_label = tk.Label(melt_frame, text='Name to use for the \'variable\' column ', bg='#282828', fg='white')
    var_name_label.place(x=10, y=130)
    
    var_name_input = ttk.Entry(melt_frame, width=10)
    var_name_input.place(x=265, y=130)
    
    # value_name label & input
    value_name_label = tk.Label(melt_frame, text='Name to use for the \'value\' column ', bg='#282828', fg='white')
    value_name_label.place(x=10, y=170)
    
    value_name_input = ttk.Entry(melt_frame, width=10)
    value_name_input.place(x=250, y=170)
    
    # submit button
    melt_submit_button = ttk.Button(melt_frame, text='Submit', command=lambda: submit_values({'id_vars': id_vars_input.get(), 'value_vars': value_vars_input.get(), 'var_name': var_name_input.get(), 'value_name': value_name_input.get()}, melt_data, data_select))
    melt_submit_button.place(x=525, y=200)
    
    
def pivot_labels(pivot_frame, data_select):
    # columns label & input
    columns_label3 = tk.Label(pivot_frame, text='Column to use to make new frame\'s columns : {str, object, list of strs} ', bg='#282828', fg='white')
    columns_label3.place(x=10, y=30)
    
    columns_input3 = ttk.Entry(pivot_frame, width=15)
    columns_input3.place(x=460, y=30)
    
    # index label & input
    index_label = tk.Label(pivot_frame, text='Column to use to make new frame\'s index : {str, object, list of strs}', bg='#282828', fg='white')
    index_label.place(x=10, y=80)
    
    index_input = ttk.Entry(pivot_frame, width=15)
    index_input.place(x=445, y=80)  
    
    # values label & input
    values_label = tk.Label(pivot_frame, text='Column(s) to use for populating new frame\'s values {str, object}', bg='#282828', fg='white')
    values_label.place(x=10, y=130)
    
    values_input = ttk.Entry(pivot_frame, width=15)
    values_input.place(x=435, y=130)
    
    # submit button
    pivot_submit_button = ttk.Button(pivot_frame, text='Submit', command=lambda: submit_values({'column': columns_input3.get(), 'index': index_input.get(), 'values': values_input.get()}, pivot_data, data_select))
    pivot_submit_button.place(x=525, y=200)
    

def aggregate_labels(aggregate_frame, data_select):
    # func label & input
    func_label = tk.Label(aggregate_frame, text='Function(s) to use for aggreagting the data : {sum, mean, median, min, max} ', bg='#282828', fg='white')
    func_label.place(x=10, y=30)
    
    func_input = ttk.Entry(aggregate_frame, width=12)
    func_input.place(x=500, y=30)
    
    # column label & input
    column_label = tk.Label(aggregate_frame, text='Column to aggregate over ', bg='#282828', fg='white')
    column_label.place(x=10, y=80)
    
    column_input = ttk.Entry(aggregate_frame, width=10)
    column_input.place(x=200, y=80)
    
    # submit button
    aggregate_submit_button = ttk.Button(aggregate_frame, text='Submit', command=lambda: submit_values({'func': func_input.get(), 'column': column_input.get()}, aggregate_data, data_select))
    aggregate_submit_button.place(x=525, y=200)
    

# labels for Clean tab (inner container in Clean tab)
def missing_values_labels(missing_values_frame, data_select):
    # Axis label & input
    axis_label = tk.Label(missing_values_frame, text='axis : {0 for index, 1 for column} ', bg='#282828', fg='white')  
    axis_label.place(x=10, y=30) 
    
    axis_input = ttk.Entry(missing_values_frame, width=10)
    axis_input.place(x=225, y=30)
    
    # how label & input
    how_label = tk.Label(missing_values_frame, text="how : {\'any', \'all\'} ", bg='#282828', fg='white')
    how_label.place(x=10, y=80)
    
    how_input = ttk.Entry(missing_values_frame, width=10)
    how_input.place(x=140, y=80)
    
    # ignore index label & input
    ignore_index_label = tk.Label(missing_values_frame, text='ignore index : {True, False}', bg='#282828', fg='white')
    ignore_index_label.place(x=10, y=130)    
    
    ignore_index_input = ttk.Entry(missing_values_frame, width=10)
    ignore_index_input.place(x=200, y=130)
    
    # submit button
    missing_values_submit_button = ttk.Button(missing_values_frame, text='Submit', command=lambda: submit_values({'axis': axis_input.get(), 'how': how_input.get(), 'ignore_index': ignore_index_input.get()}, dropna, data_select))
    missing_values_submit_button.place(x=500, y=150)
    
    
def duplicate_data_labels(duplicate_data_frame, data_select):
    # subset label & input
    subset_label = tk.Label(duplicate_data_frame, text='Column : {column name or sequence of columns seperated by spaces}', bg='#282828', fg='white')
    subset_label.place(x=10, y=30)
    
    subset_input = ttk.Entry(duplicate_data_frame, width=15)
    subset_input.place(x=460, y=30)
    
    # keep  label & input"
    keep_label = tk.Label(duplicate_data_frame, text="Keep : {\'first\', \'last\', False}", bg='#282828', fg='white')
    keep_label.place(x=10, y=70)
    
    keep_input = ttk.Entry(duplicate_data_frame, width=10)
    keep_input.place(x=195, y=70)
    
    # ignore index label & input
    ignore_index_label2 = tk.Label(duplicate_data_frame, text='ignore index : {True, False}', bg='#282828', fg='white')
    ignore_index_label2.place(x=10, y=120)    
    
    ignore_index_input2 = ttk.Entry(duplicate_data_frame, width=10)
    ignore_index_input2.place(x=200, y=120)
    
    # submit button
    drop_duplicates_submit_button = ttk.Button(duplicate_data_frame, text='Submit', command=lambda: submit_values({'subset': subset_input.get(), 'keep': keep_input.get(), 'ignore_index': ignore_index_input2.get()}, drop_duplicates, data_select))
    drop_duplicates_submit_button.place(x=500, y=150)
    

def data_type_labels(data_type_frame, data_select):
    # column label & input
    column_label = tk.Label(data_type_frame, text='Column to convert ', bg='#282828', fg='white')
    column_label.place(x=10, y=30)
    
    column_input = ttk.Entry(data_type_frame, width=10)
    column_input.place(x=150, y=30)
    
    #dtype label & input
    dtype_label = tk.Label(data_type_frame, text="Data Type : {str, int, float} ", bg='#282828', fg='white')
    dtype_label.place(x=10, y=80)
    
    dtype_input = ttk.Entry(data_type_frame, width=10)
    dtype_input.place(x= 200, y=80)
    
    # submit button
    data_type_submit_button = ttk.Button(data_type_frame, text='Submit', command=lambda: submit_values({'column': column_input.get(), 'dtype': dtype_input.get()}, astype, data_select))
    data_type_submit_button.place(x=495, y=150)
    
    
def text_cleaning_labels(text_cleaning_frame, data_select):
    # column label & input
    column_label2 = tk.Label(text_cleaning_frame, text='Column to convert text from ', bg='#282828', fg='white')
    column_label2.place(x=10, y=30)
    
    column_input2 = ttk.Entry(text_cleaning_frame, width=10)
    column_input2.place(x=215, y=30)
    
    # characters to remove
    char_label = tk.Label(text_cleaning_frame, text="Text to remove : {\' \', \'-\', \'hello\', etc.} ", bg='#282828', fg='white')
    char_label.place(x=10, y=80)
    
    char_input = ttk.Entry(text_cleaning_frame, width=10)
    char_input.place(x=265, y=80)
    
    # characters to replace with
    new_char_label = tk.Label(text_cleaning_frame, text="Text to replace with : {\' \', \'-\', \'hello\', etc.}", bg='#282828', fg='white')
    new_char_label.place(x= 10, y=130)
    
    new_char_input = ttk.Entry(text_cleaning_frame, width=10)
    new_char_input.place(x=290, y=130)
    
    # submit button
    text_cleaning_button = ttk.Button(text_cleaning_frame, text='Submit', command=lambda: submit_values({'column': column_input2.get(), 'char_input': char_input.get(), 'new_char': new_char_input.get()}, text_cleaning, data_select))
    text_cleaning_button.place(x=495, y=150)
    
    
def column_operations_labels(column_operations_frame, data_select):
    # Column label & input
    column_label3 = tk.Label(column_operations_frame, text='Rename Column : {column name}', bg='#282828', fg='white')
    column_label3.place(x=10, y=30)
    
    column_input3 = ttk.Entry(column_operations_frame, width=10)
    column_input3.place(x=250, y=30)
    
    # Rename label & input
    rename_label = tk.Label(column_operations_frame, text='Rename to : {str, int} ', bg='#282828', fg='white')
    rename_label.place(x=375, y=30)
    
    rename_input = ttk.Entry(column_operations_frame, width=10)
    rename_input.place(x= 530, y=30)
    
    # drop_column label & input
    drop_column_label = tk.Label(column_operations_frame, text='Drop column(s) : {column name(s)}', bg='#282828', fg='white')
    drop_column_label.place(x=10, y=100)
    
    drop_column_input = ttk.Entry(column_operations_frame, width=10)
    drop_column_input.place(x=230, y=100)
    
    # submit button
    rename_column_button = ttk.Button(column_operations_frame, text='Submit', command=lambda: submit_values({'column': column_input3.get(), 'rename_to': rename_input.get(), 'drop_column': drop_column_input.get()}, column_operations, data_select))
    rename_column_button.place(x=495, y=150)
    

# High order function for submit button
def submit_values(values, function, data_select):
    return function(values, data_select)


def sort_data(values, data_select):
    # Default values
    sort_by = values.get('sort_by', '')
    ascending = True
    kind = values.get('kind', 'quicksort')

    # Check input values
    if values['ascending'] == 'False':
        ascending = False
    
    if not sort_by:
        print("no input for sort_by")
        return
    
    # Split input into a list
    sort_by_values = sort_by.split(' ')
    
    df = data_select.df
    
    # Check if column exists in DataFrame
    for col in sort_by_values:
        if col not in df.columns:
            print(f"column '{col}' does not exist in DataFrame")
            return
    
    df.sort_values(by=sort_by_values, ascending=ascending, kind=kind, inplace=True)
    data_select.update_df(df)
    
    print('sort_data successful')
    
    
def melt_data(values, data_select):
    # Default values
    id_vars = values.get('id_vars', '')
    value_vars = values.get('value_vars', '')
    var_name = values.get('var_name', None)
    value_name = values.get('value_name', 'value')
    
    # Check input values
    if not id_vars:
        print('no input for id_vars')
        return
    elif not value_vars:
        print('no input for value_vars')
        return
    
    # Convert strings into list
    id_vars_values = id_vars.split(' ')
    value_vars_values = value_vars.split(' ')
    
    df = data_select.df
    
    # Check if values are in DataFrame
    for col in id_vars_values + value_vars_values:
        if col not in df.columns:
            print(f"column '{col}' does not exist in DataFrame")
            return
    
    new_df = pd.melt(df, id_vars=id_vars_values, value_vars=value_vars_values, var_name=var_name, value_name=value_name)
    data_select.update_df(new_df)
    
    print('melt successful')
    
    
def pivot_data(values, data_select):
    # Default values
    column = values.get('column', '')
    index = values.get('index', '')
    values = values.get('values', '')
    
    # Check input values for columns
    if not column:
        print('no input for columns')
        return
    
    df = data_select.df
    
    # Split string into list
    column_values = column.split(' ')
    index_values = index.split(' ')
    
    # Check if columns exist in DataFrame
    for col in column_values + index_values:
        if col not in df.columns:
            print(f"column '{col}' does not exist in DataFrame")
            return
        
    new_df = df.pivot(index=index_values, columns=column_values, values=values)
    data_select.update_df(new_df)
    
    print('pivot_data successful')


def aggregate_data(values, data_select):
    # Default values
    func = values.get('func', '')
    column = values.get('column', '')
    
    # Check values in func
    if not func:
        print('no input for func')
        return
    elif not column:
        print('no input for column')
        return
    
    # Split strings into list
    func_values = func.split(' ')
    
    # Validate aggregation functions
    valid_agg_funcs = ['sum', 'mean', 'median', 'min', 'max']
    for f in func_values:
        if f not in valid_agg_funcs:
            print(f"'{f}' is not a valid aggregation function")
            return
            
    df = data_select.df
    
    # Check if column exists in DataFrame
    if column not in df.columns:
        print(f"columns {column} does not exist in DataFrame")
    
    new_df = df.agg({column : func_values})
    data_select.update_df(new_df)
    
    print('aggregate_data successful')
    
    
def dropna(values, data_select):
    # Default values
    axis: int = int(values.get('axis', 0))
    how: str = values.get('how', 'any')
    ignore_index: bool = False
    
    if values['ignore_index'] == 'True':
        ignore_index = True

    df = data_select.df
    new_df = df.dropna(axis=axis, how=how, ignore_index=ignore_index)
    data_select.update_df(new_df)
    
    print("dropna successful")


def drop_duplicates(values, data_select):
    # Default values
    subset: str = values.get('subset', '')
    keep = values.get('keep', 'first')
    ignore_index: bool = False
    
    if values['keep'] == 'False':
        keep = False        
    
    if values['ignore_index'] == 'True':
        ignore_index = True

    df = data_select.df   
    if subset:
        # Create list based on input seperated by spaces
        subset_list = subset.split(" ")
        new_df = df.drop_duplicates(subset=subset_list, keep=keep, ignore_index=ignore_index)
        data_select.update_df(new_df)
    else:
        # if subset parameter is empty
        new_df = df.drop_duplicates(keep=keep, ignore_index=ignore_index)
        data_select.update_df(new_df)
        
    print('drop_duplicates successful')
    
    
def astype(values, data_select):
    # Default values
    col = values.get('column', '')
    dtype = values.get('dtype', '')
    
    # Check input values
    if not col:
        print('no input for column')
        return
    elif not dtype:
        print('no input for dtype')
        return
    
    df = data_select.df
    
    # Check if column exists in DataFrame
    if col not in df.columns:
        print(f'column {col} does not exist in the DataFrame')
        return
    
    df.col = df.astype({col: dtype}).dtypes
    data_select.update_df(df)
    
    print('astype successful')
    
    
def text_cleaning(values, data_select):
    # Default values
    col = values.get('column', '')
    char_input = values.get('char_input', '')
    char_output = values.get('new_char', '')
    
    # Check input values
    if not col:
        print('no input for column')
        return
    elif not char_input:
        print('no input for char input')
        return      
    
    df = data_select.df
    
    # Check if column exists in DataFrame
    if col not in df.columns:
        print(f'column {col} does not exist in the DataFrame')
        return    
    
    # Print out to console if characters were successfully replaced
    if df[col].str.contains(char_input).any():
        df[col] = df[col].iloc[:].str.replace(char_input, char_output)
        data_select.update_df(df)
        print(f"Replaced '{char_input}' with '{char_output}' in column '{col}'")
    else:
        print(f"Could not find {char_input} in '{col}'")
        return


def column_operations(values, data_select):
    # Default values
    col = values.get('column', '')
    rename_value = values.get('rename_to', '') 
    drop_column = values.get('drop_column', '')
    
    # Check input values
    if not col and not drop_column:
        print('no input for column to rename and column to drop')
        return
    
    if col and not rename_value:
        print('no input for renaming value')
        return
    elif rename_value and not col:
        print('no input for column to rename')
        return

    df = data_select.df
    
    # Rename column
    if col:
        if col not in df.columns:
            print(f'column {col} does not exist in DataFrame')
            return
        df.rename(columns={col: rename_value}, inplace=True)
        data_select.update_df(df)
        print(f"column '{col}' renamed to '{rename_value}'")
    
    # Drop column
    if drop_column:
        drop_columns = drop_column.split(' ')
        for col in drop_columns:
            if col not in df.columns:
                print(f"column '{col}' does not exist in DataFrame")
                return
        df.drop(columns=drop_columns, inplace=True)
        data_select.update_df(df)
        print(f"columns '{', '.join(drop_columns)}' dropped")
