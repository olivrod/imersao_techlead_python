import base64
import sys

def decode_image(base64_str: str) -> bytes:
    """
    Decode a base64 encoded image string into bytes.
    
    Args:
        base64_str (str): The base64 encoded image string.
        
    Returns:
        bytes: The decoded image bytes.
    """
    return base64.b64decode(base64_str)

if __name__ == "__main__":
    if sys.argv.__len__() > 1:
        txtfilepath = sys.argv[1]
        image_bytes = None
        image_file_name_jpg = None

        if not txtfilepath.endswith(".txt"):
            print("Please provide a .txt file containing the base64 encoded image.")
            sys.exit(1)
        
        with open(txtfilepath, "r") as f:
            base64_str = f.read()
            base64_str_replace = base64_str.replace('data:image/jpeg;base64,', '')
            image_bytes = decode_image(base64_str_replace)
            image_file_name_jpg = txtfilepath.replace(".txt", ".jpg")

        if image_bytes is None:
            print("No image data found in the provided file.")
            sys.exit(1)

        if image_file_name_jpg is None:
            print("No image file name generated.")
            sys.exit(1)
            
        with open(image_file_name_jpg, "wb") as fb:
            fb.write(image_bytes)
            print(f"{image_file_name_jpg} saved!")
    
    
    