path = "C:/Users/Administrator/Desktop/"
csv_name = "test.csv"
csvFile = open(path + csv_name, newline='')

from load_csv import *

row_list = Initialize_test_table(csvFile)
print(row_list)
print(len(row_list))