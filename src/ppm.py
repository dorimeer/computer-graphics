from src.image import Image


class Ppm:
    @staticmethod
    def read(name):
        with open(name, 'rb') as ppm_file:
            return [row for row in ppm_file.readlines()]

    @staticmethod
    def clean(input_img):
        output_img = []
        for row in input_img:
            output_img.append(row.decode())
        for row in output_img:
            if '#' in row:
                output_img.remove(row)
        return output_img

    @staticmethod
    def data(input_img):
        new_format = ' '.join(input_img)
        size = new_format.split()[1:3]
        size = list(map(int, size))

        pixels = new_format.split()[4:]
        pixels = list(map(int, pixels))
        chunks = [pixels[i:i + 3] for i in range(0, len(pixels), 3)]

        image_data = Image(
            size[0],
            size[1],
            chunks,
        )

        return image_data

    @staticmethod
    def write_from_bmp(img_data, result_directory):
        format = 'P3 \n'
        size = str(img_data.width) + ' ' + str(img_data.height) + '\n'

        chunks = []
        for row in img_data.pixel_map:
            chunks += row

        _max = max(chunks)
        _max = str(_max) + '\n'

        new_arr = img_data.pixel_map

        new_chunks = []
        new_order = []
        count = 0
        for chunk in new_arr:
            new_order.append(chunk)
            count += 1
            if count == img_data.width:
                new_order.reverse()
                new_chunks += new_order
                new_order = []
                count = 0
        new_chunks.reverse()
        s = ''
        for chunk in new_chunks:
            chunk = ' '.join([str(i) for i in chunk])
            s += chunk + '\n'

        file = format + size + _max + s

        result_directory = str(result_directory)
        with open(result_directory, 'w+') as ppm_file:
            ppm_file.write(file)

    @staticmethod
    def write_from_png(img_data, result_directory):
        format_ = 'P3 \n'
        size = str(img_data.width) + ' ' + str(img_data.height) + '\n'
        _max = max(img_data.pixel_map)
        _max = str(_max)
        s = ' '.join([str(i) for i in img_data.pixel_map])
        file = format_ + size + _max + ' ' + s

        result_directory = str(result_directory)
        with open(result_directory, 'w+') as ppm_file:
            ppm_file.write(file)
