import os 
import pandas as pd 
import csv  

def print_current_sudoku(df):
    df_formatted = df.applymap(lambda x: '{:.0f}'.format(x) if isinstance(x, (int, float)) else x)
    print(df_formatted)

if __name__ == "__main__":
    df = pd.read_excel("Sudoku.xlsx")
    print_current_sudoku(df)