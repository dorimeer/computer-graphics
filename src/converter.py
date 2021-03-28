from src.bmp import Bmp
from src.png import Png
from src.ppm import Ppm


class Converter:
    def start(self):
        print('Specify input file and choose output format'
              'Example: --source=example.bmp --goal-format=ppm --output=result.ppm')
        user_input = input()
        source = ''
        source_format = ''
        output_directory = ''
        try:
            source = user_input.split()[0][9:]
            source_format = source.split('.')[-1]
            goal_format = user_input.split()[1][14:]
            print(source)
            print(source_format)
            print(goal_format)
            if goal_format != 'ppm':
                print('Unsupported output format')
                self.start()
            output_directory = source.split('.')[0] + '.ppm'
            if 'output' in user_input:
                output_directory = user_input.split()[2][9:]
        except Exception:
            print('Invalid input. Try again.')
            self.start()

        if source_format == 'png':
            try:
                png_converter = Png()
                ppm_converter = Ppm()
                png_image = png_converter.read(source)
                ppm_converter.write_from_png(png_image, output_directory)
            except FileNotFoundError:
                print("Couldn't find the .png file specified. Try again.")
                self.start()
        elif source_format == 'bmp':
            try:
                bmp_converter = Bmp()
                ppm_converter = Ppm()
                bmp_image = bmp_converter.read(source)
                ppm_converter.write_from_bmp(bmp_image, output_directory)
            except FileNotFoundError:
                print("Couldn't find the .bmp file specified. Try again.")
                self.start()
        else:
            print('Unsupported source format. Try again')
            self.start()
