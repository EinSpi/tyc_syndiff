import os
import shutil
import random

def move_random_files(source_folder, target_folder, num_files):
    # Ensure the target folder exists; if not, create it
    os.makedirs(target_folder, exist_ok=True)
    
    # Get a list of all files in the source folder
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    
    # Ensure there are enough files to select
    if num_files > len(files):
        print(f"Error: The source folder contains only {len(files)} files, which is less than the requested {num_files} files.")
        return
    
    # Randomly select files
    selected_files = random.sample(files, num_files)
    
    # Move each selected file to the target folder
    for file_name in selected_files:
        source_path = os.path.join(source_folder, file_name)
        target_path = os.path.join(target_folder, file_name)
        shutil.move(source_path, target_path)
        print(f"Moved {file_name} to {target_folder}")

# Example usage
source_folder = 'E:\\WS2324\\praktikum\\real_us_imgs_all_256_resized'  # Replace with the path to your source folder
target_folder = 'E:\\WS2324\\praktikum\\real_us_imgs_all_256_resized\\VAL'  # Replace with the path to your target folder
num_files_to_move = 480  # Set the number of files you want to move

move_random_files(source_folder, target_folder, num_files_to_move)
