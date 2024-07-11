import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Read Excel file
excel_file_path = 'names.xlsx'
excel_file = pd.ExcelFile(excel_file_path)
sheet_names = excel_file.sheet_names

# Load bg images
bg_folder_name = 'bg'
all_files = os.listdir(bg_folder_name)
image_files = [file for file in all_files if os.path.isfile(os.path.join(bg_folder_name, file)) and file.lower().endswith('.png')]
image_files = [os.path.join(bg_folder_name, file) for file in image_files]
images = [Image.open(file) for file in image_files]

# output folder
output_folder = 'output'
os.makedirs(output_folder, exist_ok=True)

def write_name_to_image(image, name):
    name = str(name)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("font/static/NotoSansThai-Bold.ttf", 350)

    # Calculate text size and position
    text_bbox = draw.textbbox((0, 0), name, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (image.width - text_width) // 2
    text_y = (image.height - text_height) // 100 * 45

    # Write text to the image
    draw.text((text_x, text_y), name, fill="black", font=font, align="center")

    return image

for sheet_name in sheet_names:
    data_col = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    names = data_col.iloc[:, 1] # Read on column B (index = 1)

    # Create folder for each sheet
    output_department_folder = os.path.join(output_folder, sheet_name)
    os.makedirs(output_department_folder, exist_ok=True)

    for bg_image in images:
        if sheet_name.lower() in bg_image.filename.lower():
            for i, name in enumerate(names):
                image = bg_image.copy()
                updated_image = write_name_to_image(image, name)
                output_path = os.path.join(output_department_folder, f'{sheet_name}-{i+1}-{name}.png')
                updated_image.save(output_path)
            
            break

print("Images saved successfully.")