from IT8951.display import AutoEPDDisplay
from IT8951 import constants
from PIL import Image
from postprocess import *


def update_image(filename, vcom_val = -2.00):

    do_image_generation(1448,1072,filename)

    display = AutoEPDDisplay(vcom=vcom_val, rotate=None, mirror=False, spi_hz=24000000)
    for _ in range(2):
        display.clear()

    display.frame_buf.paste(0xFF, box=(0, 0, display.width, display.height))

    img = Image.open("output.bmp")

    dims = (display.width, display.height)

    img.thumbnail(dims)
    paste_coords = [dims[i] - img.size[i] for i in (0,1)]  # align image with bottom of display
    display.frame_buf.paste(img, paste_coords)

    for _ in range(5):
        display.draw_full(constants.DisplayModes.GC16)
