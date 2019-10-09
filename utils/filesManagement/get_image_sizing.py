from PIL import Image


def get_image_sizing(image_file_path):
    """
    Function to retrieve the picture sizing
    :param image_file_path: Type file picture
    :return: tuple with height and width of the selected picture
    """

    picture = Image.open(image_file_path)
    return picture.size
