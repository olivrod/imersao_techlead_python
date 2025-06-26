from PIL import __version__ as pillow_version

def lambda_handler(event, context):
    return {"message": pillow_version}