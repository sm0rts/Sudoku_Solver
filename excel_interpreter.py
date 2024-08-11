import os 
import pandas as pd 
import csv  

class cell:
    pass

def print_current_sudoku(df):
    df_formatted = df.map(lambda x: '{:.0f}'.format(x) if isinstance(x, (int, float)) else x)
    print(df_formatted)

def convert_sudoku_to_data_frame(file_path):
    file_ending = file_path.split(".")[-1]
    if file_ending == "xlsx":
        df = pd.read_excel("Sudoku.xlsx")
    return(df)

if __name__ == "__main__":
    df = convert_sudoku_to_data_frame("Sudoku.xlsx")
    print_current_sudoku(df)