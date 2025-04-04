import os

# Define the root directory containing pest folders
root_dir = "./"

# Counter for deleted files
deleted_count = 0

# Traverse directories and remove .gif images
for foldername, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.lower().endswith(".gif"):
            gif_path = os.path.join(foldername, filename)
            
            try:
                os.remove(gif_path)  # Delete the file
                print(f"🗑️ Deleted: {gif_path}")
                deleted_count += 1
            except Exception as e:
                print(f"❌ Error deleting {gif_path}: {e}")

# Print summary
if deleted_count > 0:
    print(f"\n✅ Successfully deleted {deleted_count} .gif images.")
else:
    print("\n✅ No .gif images found!")
