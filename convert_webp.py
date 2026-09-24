import os
from PIL import Image

def convert_to_webp():
    directory = r"d:\Daniportfoli\portfolio\assets\images\projects"
    for filename in os.listdir(directory):
        if filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(".jpg"):
            filepath = os.path.join(directory, filename)
            # Create a new filename with .webp extension
            webp_filename = os.path.splitext(filename)[0] + ".webp"
            webp_filepath = os.path.join(directory, webp_filename)
            
            try:
                img = Image.open(filepath)
                # Convert to RGB if it's RGBA and we want to save as JPEG, 
                # but WebP supports RGBA so it's fine.
                img.save(webp_filepath, "webp", quality=85)
                print(f"Converted {filename} to {webp_filename}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    convert_to_webp()
