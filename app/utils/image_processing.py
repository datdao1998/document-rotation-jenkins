from PIL import Image

def normalize_image(image: Image, max_size: int=1600) -> Image:
    """Normalize size of image input

    :param image: Input image
    :type image: Image
    :param max_size: The maxium length of resized image, defaults to 1600
    :type max_size: int, optional
    :return: Resized image
    :rtype: PIL.Image
    """
    width, height = image.size

    if width > height:
        new_width = max_size
        new_height = int((height/width) * new_width)
    else:
        new_height = max_size
        new_width = int((width/height) * new_height)
    
    resized_image = image.resize((new_width, new_height))

    return resized_image