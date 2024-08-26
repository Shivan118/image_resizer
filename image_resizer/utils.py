from PIL import Image
import base64
import io

def resize_image(image, width, height):
    return image.resize((width, height), Image.LANCZOS)

def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')
