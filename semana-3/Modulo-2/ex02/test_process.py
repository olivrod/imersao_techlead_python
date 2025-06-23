import pytest
from process import process_image
from PIL import Image

@pytest.fixture
def sample_image():
    """
    Fixture to create a sample image for testing.
    """
    img = Image.new('RGB', (600, 400), color='blue')
    return img

def test_process_image_with_large_image(sample_image):
    """
    Test processing a large image to ensure it resizes and converts to grayscale.
    """
    processed_image = process_image(sample_image)
    
    # Check if the image is resized correctly
    assert processed_image.size[0] <= 500 and processed_image.size[1] <= 500
    
    # Check if the image is converted to grayscale
    assert processed_image.mode == 'L'