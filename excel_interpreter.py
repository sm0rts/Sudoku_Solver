import os 
import pandas as pd 
import csv  

class cell:
    def __init__(self, row , column, value = 0):
        self.row = row
        self.column = column
        self.value = value
        self.possible_values = [1,2,3,4,5,6,7,8,9]

    def identify(self):
        print()
        print("Row: \t\t" + str(self.row))
        print("Column: \t" + str(self.column))
        if self.value != (0 or "nan"):
            print("Value: \t\t" + str(self.value))
        else :
            print("Possible values: " + str(self.possible_values))

def print_current_sudoku(df):
    df_without_row_0=df.drop(0)
    print(df_without_row_0)

def convert_sudoku_to_data_frame(file_path):
    file_ending = file_path.split(".")[-1]
    if file_ending == "xlsx":
        df = pd.read_excel("Sudoku.xlsx")
        df_formatted = df.map(lambda x: '{:.0f}'.format(x) if isinstance(x, (int, float)) else x)
    return(df_formatted)

if __name__ == "__main__":
    df = convert_sudoku_to_data_frame("Sudoku.xlsx")
    print_current_sudoku(df)
    cells = []
    for row in range(1,10):
        for column in range(1,10):
            #cell_identifier = f"cell{row,column}"
            cell_instance = cell(row,column,df.iloc[row,column])
            cells.append(cell_instance)
    for cell_instance in cells:
        cell_instance.identify()

    value = df.iloc[8,9]
    print()
    cell1 = cell(1,4)
    cell1.identify()