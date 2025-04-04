import os

# Set to store unique file extensions
unique_extensions = set()
root_dir = "./"

# Loop through each class folder
for pest_class in os.listdir(root_dir):
    class_dir = os.path.join(root_dir, pest_class)
    if os.path.isdir(class_dir):  # Ensure it's a directory
        for file in os.listdir(class_dir):
            ext = os.path.splitext(file)[1].lower()  # Extract file extension
            if ext:  # Ensure there's an extension
                unique_extensions.add(ext)

# Display all unique extensions found
print("📌 Unique file extensions in the dataset:", unique_extensions)