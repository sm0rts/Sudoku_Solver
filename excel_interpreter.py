import os 
import pandas as pd 
import csv  

class cell:
    possible_values_of_rows = [[0 for _ in range(9)] for _ in range(9)]
    possible_values_of_columns = [[0 for _ in range(9)] for _ in range(9)]
    possible_values_of_sectors = [[0 for _ in range(9)] for _ in range(9)]
    @classmethod
    def init_row_data (cls):
        for i in range (9):
            for j in range (9):
                cls.possible_values_of_rows[i][j] = j+1
                cls.possible_values_of_columns[i][j] = j+1
                cls.possible_values_of_sectors[i][j] = j+1

    def __init__(self, row , column, value = 0):
        self.row = row
        self.column = column
        self.value = value
        self.sector = 3*int((row-1)/3)+int((column-1)/3)+1
        self.sector_pos = 3*(row-3*int((row-1)/3)-1) + column-3*int((column-1)/3)
        self.possible_values = [1,2,3,4,5,6,7,8,9]

    def remove_value_from_array(array,value):
        array.remove(value)


    def remove_used_values_from_group(group):
        if (group == row): 
            observed_group = cell.possible_values_of_rows
        for instance_of_observed_group in observed_group:
            for unseen_value in instance_of_observed_group:
                return(0)
             


    def identify(self):
        print()
        print("Row: \t\t" + str(self.row))
        print("Column: \t" + str(self.column))
        print("Sector: \t" + str(self.sector))
        print("Sector_pos: \t" + str(self.sector_pos))
        if self.value != (0 or "nan"):
            print("Value: \t\t" + str(self.value))
        else :
            print("Possible values: " + str(self.possible_values))

    def check_group(self, group):
        if group == "row":
            matching_cells = [cell for cell in cells if cell.row == self.row]
            for cell in matching_cells:
                cell.identify()
        elif group == "column":
            pass
        elif group == "cage":
            pass

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
    rows = [[None for _ in range(0,10)] for _ in range(0,10)]
    columns = [[None for _ in range(0,10)] for _ in range(0,10)]
    sectors = [[None for _ in range(0,10)] for _ in range(0,10)]
    for row in range(1,10):
        for column in range(1,10):
            print("row: " + str(row) + " column: " + str(column))
            cell_instance = cell(row,column,df.iloc[row,column])
            cells.append(cell_instance)
            rows    [row][column] =                     cell_instance
            columns [column][row] =                     cell_instance
            sectors [cell_instance.sector][column] =    cell_instance
            cell_instance.identify()
    cell.init_row_data()
    columns[9][2].identify()
