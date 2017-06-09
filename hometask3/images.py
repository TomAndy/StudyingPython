
import os
from PIL import Image

path_to_images = "d:/images/"
path_converted_images = "d:/images_black/"


def read_image_files(path_to_images):
    imagelist = []
    for filelist in os.listdir(path_to_images):
        imagelist.append(filelist)
    return imagelist


def convert_images(list_of_images, path_to_converted_images):
    for image in list_of_images:
        image_file = Image.open(os.path.join(path_to_images, image))
        newim = image_file.convert('1')
        newim = newim.rotate(90)
        newim.save(path_to_converted_images + image)


def clear_folder(path):
    for file_item in os.listdir(path):
        if file_item:
            os.remove(os.path.join(path, file_item))


if __name__ == '__main__':
    list_of_images = read_image_files(path_to_images)
    clear_folder(path_converted_images)
    convert_images(list_of_images, path_converted_images)
