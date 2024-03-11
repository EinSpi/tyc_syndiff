import os
from PIL import Image

def resize_image(input_path, output_dir, filename):
    try:
        with Image.open(input_path) as img:
            img = img.resize((256, 256), Image.ANTIALIAS)
            # Ensure the output directory exists
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            output_path = os.path.join(output_dir, filename)
            img.save(output_path)
    except Exception as e:
        print(f"Error processing file {input_path}: {e}")

def traverse_and_resize(root_dir, output_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(dirpath, filename)
                # Generate a unique filename if necessary to avoid overwrites
                
                # Optional: Create a more unique name by prefixing the relative path
                relative_dir = os.path.relpath(dirpath, root_dir)
                unique_filename = f"{relative_dir.replace(os.sep, '_')}_{filename}"
                resize_image(file_path, output_dir, unique_filename)

# Replace 'your/root/directory/path' with the path to your root directory
root_directory = "E:\\WS2324\\praktikum\\real_us_imgs"
# Specify the directory where you want to save all resized images
output_directory = "E:\\WS2324\\praktikum\\real_us_imgs_all_256_resized"
traverse_and_resize(root_directory, output_directory)
