import io
import pandas as pd
import numpy as np


def retrieve_info():
    df = return_df()
    buffer = io.StringIO()
    df.info(buf=buffer)
    df_info = buffer.getvalue()
    info_list = df_info.split('\n')
    
    return info_list

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