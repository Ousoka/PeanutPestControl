import os
from PIL import Image
from tqdm import tqdm

# Define the root directory containing pest folders
root_dir = "./"

# Supported extensions
valid_extensions = {".jpeg", ".jfif", ".webp", ".gif", ".png", ".jpg"}

# Loop through all folders and files
for folder in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder)
    
    if os.path.isdir(folder_path):  # Ensure it's a folder
        print(f"Processing folder: {folder}")
        
        for filename in tqdm(os.listdir(folder_path), desc=f"Converting images in {folder}"):
            file_path = os.path.join(folder_path, filename)
            file_ext = os.path.splitext(filename)[1].lower()
            
            if file_ext in valid_extensions:  # Check if the file is an image
                try:
                    with Image.open(file_path) as img:
                        rgb_img = img.convert("RGB")  # Convert to RGB to avoid mode issues
                        new_filename = os.path.splitext(filename)[0] + ".jpg"
                        new_path = os.path.join(folder_path, new_filename)
                        
                        rgb_img.save(new_path, "JPEG", quality=95)  # Save as JPG
                        
                        if file_ext != ".jpg":
                            os.remove(file_path)  # Delete the original file
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

print("Conversion completed successfully!")
