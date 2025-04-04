import os

# Define the root directory containing pest folders
root_dir = "./"

# List to store .gif file paths
gif_images = []

# Traverse directories and find .gif images
for foldername, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.lower().endswith(".gif"):
            gif_path = os.path.join(foldername, filename)
            gif_images.append(gif_path)

# Print all .gif file paths
if gif_images:
    print("\n🚀 Found .gif images:")
    for img in gif_images:
        print(img)
else:
    print("\n✅ No .gif images found!")

# Optional: Save the paths to a text file
with open("gif_images_list.txt", "w") as file:
    file.write("\n".join(gif_images))
    print("\n📄 File 'gif_images_list.txt' saved with all .gif image paths.")
