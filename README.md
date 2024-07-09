# Nametag Generator
Python Version: 3.12.4

### Install Libraries
```bash
pip install pandas pillow openpyxl
# or
pip3 install pandas pillow openpyxl
```

## How to Use
1. Place Excel File:

- Put your Excel file (*.xlsx) in the root of the project directory.
- Rename it to names.xlsx or update the excel_file_path variable in [main.py](./main.py) on line 6 to match your Excel file name.
2. Insert Nametag Images:

- Place your nametag images in the 'bg' folder.
Set Custom Font:

3. Copy your font file (*.ttf) to the 'font' folder.
- Update the font style and font size in [main.py](./main.py) on line 24.

## Run the Script
```bash
python main.py
# or
python3 main.py
```