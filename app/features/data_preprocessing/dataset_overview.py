import io

def retrieve_info(df):
    buffer = io.StringIO()
    df.info(buf=buffer)
    df_info = buffer.getvalue()
    
    return df_info.split('\n')
    
