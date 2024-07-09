import os

# Specify the folder path
folder_path = 'bg'

# Get a list of all files and directories in the specified folder
all_files = os.listdir(folder_path)

# Filter out directories and non-.png files, only keep .png files
png_files = [file for file in all_files if os.path.isfile(os.path.join(folder_path, file)) and file.lower().endswith('.png')]

# Print the .png file names
for file in png_files:
    print(file)
