import pandas as pd

# Specify the Excel file path
excel_file_path = 'names.xlsx'

# Load the Excel file
excel_file = pd.ExcelFile(excel_file_path)

# Get all sheet names
sheet_names = excel_file.sheet_names

# Print the sheet names
for sheet_name in sheet_names:
    print(sheet_name)
