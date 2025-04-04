import os
from PIL import Image
from tqdm import tqdm

# Define the root directory containing pest folders
root_dir = "./"

# Counter for corrupt images
corrupt_images = []

# Loop through all folders and check images
for folder in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder)
    
    if os.path.isdir(folder_path):
        print(f"Checking images in folder: {folder}")
        
        for filename in tqdm(os.listdir(folder_path), desc=f"Checking {folder}"):
            file_path = os.path.join(folder_path, filename)
            
            try:
                with Image.open(file_path) as img:
                    img.verify()  # Verify if image is not corrupt
            except Exception as e:
                corrupt_images.append(file_path)
                print(f"Corrupt image found: {file_path} - {e}")

# Print summary
if corrupt_images:
    print("\n🚨 Corrupt images detected:")
    for img in corrupt_images:
        print(img)
else:
    print("\n✅ No corrupt images found. All images are working properly!")
