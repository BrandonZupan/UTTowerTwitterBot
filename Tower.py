#Brandon Zupan
#Class for UT Tower

import requests
from PIL import Image
from io import BytesIO

class Tower:
    def __init__(self):
        #Run aquire image method to get one on init
        self.image = None
        self.top_color = None
        self.base_color = None
        self.URL = "http://wwc.instacam.com/instacamimg/UTAUS/UTAUS_l.jpg"

    def set_image(self):
        """Returns an image object for further analysis"""
        img_data = requests.get(self.URL)
        tower_image = Image.open(BytesIO((img_data.content)))
        tower_image.show()

        

tower = Tower()

tower.set_image()
