# Brandon Zupan
# Class for UT Tower

import requests
from PIL import Image
from io import BytesIO


class Tower:
    def __init__(self):
        # Constants
        self.URL = "http://wwc.instacam.com/instacamimg/UTAUS/UTAUS_l.jpg"
        self.BASE_COORDINATES = (718, 217, 731, 358)
        self.TOP_COORDINATES = (695, 139, 728, 179)

        self.image = None
        self.base = self.TowerSection(*self.BASE_COORDINATES)
        self.top = self.TowerSection(*self.TOP_COORDINATES)
        
    def set_image(self):
        """Returns an image object for further analysis"""
        img_data = requests.get(self.URL)
        self.image = Image.open(BytesIO(img_data.content))
        self.image.show()

    class TowerSection:
        def __init__(self, x1, y1, x2, y2):
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2

            self.r = 0
            self.g = 0
            self.b = 0

        def find_average_color(self, picture):
            """
            Finds the average color for a section of the tower
            Input: The picture
            Sets the section's RGB values
            """
            for x in range(self.x1, self.x2):
                for y in range(self.y1, self.y2):
                    color = picture.getpixel((x, y))
                    self.r += color[0]
                    self.g += color[1]
                    self.b += color[2]

            total_pixels = (self.y2 - self.y1) * (self.x2 - self.x1)
            self.r = int(self.r/total_pixels)
            self.g = int(self.g / total_pixels)
            self.b = int(self.b / total_pixels)
