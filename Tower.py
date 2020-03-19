# Brandon Zupan
# Class for UT Tower

import requests
from PIL import Image
from io import BytesIO


class Tower:
    def __init__(self):
        # Run acquire image method to get one on init
        self.image = None
        self.top_color = None
        self.base_color = None
        
        # Constants
        self.URL = "http://wwc.instacam.com/instacamimg/UTAUS/UTAUS_l.jpg"
        self.BASE_COORDS = (718, 217, 731, 358)
        self.TOP_COORDS = (695, 139, 728, 179)
        
    def set_image(self):
        """Returns an image object for further analysis"""
        img_data = requests.get(self.URL)
        self.image = Image.open(BytesIO((img_data.content)))

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





tower = Tower()

tower.set_image()

#tower.image.show()

print(f"Top: {tower.average_color(tower.image, tower.TOP_COORDS)}")
