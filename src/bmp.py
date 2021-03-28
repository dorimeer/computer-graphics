from struct import unpack

from src.image import Image


class Bmp:
    @staticmethod
    def read(path):
        f = open(path, "rb")

        f.read(2+4+2+2+4+4)
        pixel_width = unpack('<i', f.read(4))[0]
        pixel_height = unpack('<i', f.read(4))[0]
        f.read(2+2+4+20)

        pixels = []
        padding = 4 - (3 * pixel_width) % 4
        if padding == 4:
            padding = 0

        for _ in reversed(range(pixel_height)):
            for j in range(pixel_width):
                b = unpack('<B', f.read(1))[0]
                g = unpack('<B', f.read(1))[0]
                r = unpack('<B', f.read(1))[0]
                pixels.append([r, g, b])
            for p in range(padding):
                f.read(1)

        image_data = Image(
            pixel_width,
            pixel_height,
            pixels
        )
        return image_data
