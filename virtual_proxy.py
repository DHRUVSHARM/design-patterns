# virtual proxy - we make the same call, but using a virual interface
class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f'Loading image from {filename}')

    def draw(self):
        print(f'Drawing image {self.filename}')


class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        # used to prevent multiple setup and send request to draw without loading files multiple times
        self.bitmap = None

    def draw(self):
        if not self.bitmap:
            self.bitmap = Bitmap(self.filename)
        self.bitmap.draw()

def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing image')

if __name__ == '__main__':
    bmp = LazyBitmap('facepalm.jpg')  # Bitmap
    draw_image(bmp)
    draw_image(bmp)
    draw_image(bmp)
