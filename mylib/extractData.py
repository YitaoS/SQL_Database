import pandas as pd

def extract_data(file_path):
    data = pd.read_csv(file_path,delimiter='\t',encoding="utf-16",on_bad_lines='skip')
    return data
