import io
import hashlib
from PIL import ImageGrab
import time
import os

# Specify the directory where you want to save the images
save_directory = "d:\\clipboard"

def get_image_hash(img):
    """
    Computes and returns a hash for a given PIL Image object.
    """
    img_byte_array = io.BytesIO()  # Use BytesIO as an in-memory binary stream
    img.save(img_byte_array, format='PNG')
    return hashlib.sha256(img_byte_array.getvalue()).hexdigest()

def save_clipboard_image(filename, last_image_hash):
    """
    Saves the image in the clipboard to a file with the specified filename,
    if the image is different from the last saved image.
    Returns the hash of the saved image and a boolean indicating if a save occurred.
    """
    try:
        # Grab the image from the clipboard
        img = ImageGrab.grabclipboard()
        if img is None:
            #print("No image in clipboard!")
            return last_image_hash, False

        current_image_hash = get_image_hash(img)
        
        # Check if the current image is different from the last saved image
        if current_image_hash == last_image_hash:
            #print("Image in clipboard is the same as the last saved image. Skipping save.")
            return last_image_hash, False
        
        # Ensure the save directory exists
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        
        # Construct the full path where the image will be saved
        full_path = os.path.join(save_directory, filename)
        
        # Save the image
        img.save(full_path, 'PNG')
        print(f"Image saved as {full_path}")
        return current_image_hash, True
    except Exception as e:
        print(f"Error saving image: {e}")
        return last_image_hash, False

def main():
    last_saved_image_hash = ""
    check_interval = 5  # seconds

    while True:
        time.sleep(check_interval)
        
        # Generate a filename with a timestamp to ensure uniqueness
        filename = f"clipboard_{int(time.time())}.png"
        
        # Attempt to save the current clipboard image, if it's new
        last_saved_image_hash, _ = save_clipboard_image(filename, last_saved_image_hash)

if __name__ == "__main__":
    main()
