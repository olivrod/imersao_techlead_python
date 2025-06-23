import sys
from PIL import Image

def process_image(image: Image.Image) -> Image.Image:
    """
    Process the image to keep the size ratio up to 500x500 pixels and convert it to grayscale.
    
    Args:
        image (Image.Image): The input image to process.
        
    Returns:
        Image.Image: The processed image.
    """
    response = image
    
    if image.width > 500 or image.height > 500:
        # Resize the image while maintaining the aspect ratio
        response.thumbnail((500, 500))
    else:
        print("Image is already within the size limits.")

    return response.convert("L")  # Convert to grayscale
    

if __name__ == "__main__":
    """
    Receives an image file path from the command line, processes the image,
    and saves the processed image with a suffix "_converted.jpg" in the same directory.
    """
    if len(sys.argv) != 2:
        print("Usage: python process.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    
    try:
        with Image.open(image_path) as img:
            processed_image = process_image(img)
            output_path = image_path.rsplit('.', 1)[0] + "_converted.jpg"
            processed_image.save(output_path)
            print(f"{output_path} saved!")
    except Exception as e:
        print(f"Error processing image: {e}")
        sys.exit(1)
    