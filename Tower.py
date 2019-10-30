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
        
        #Constants
        self.URL = "http://wwc.instacam.com/instacamimg/UTAUS/UTAUS_l.jpg"
        self.BASE_COORDS = (718, 217, 731, 358)
        self.TOP_COORDS = (695, 139, 728, 179)
        
        

    def set_image(self):
        """Returns an image object for further analysis"""
        img_data = requests.get(self.URL)
        self.image = Image.open(BytesIO((img_data.content)))

        
    def average_color(self, picture, COORDS):
        """Find average color of an area of a picture"""
        r = 0
        g = 0
        b = 0
        color = 0

        #victim = picture.crop(COORDS)
        #victim.show()

        #Iterate through pixels
        #print(range(COORDS[0], COORDS[2]))
        print(picture.size)
        for y in range(COORDS[0], COORDS[2]):
            for x in range(COORDS[1], COORDS[3]):
                #print(f"x{x} y{y} ")
                color = picture.getpixel((x,y))
                r = r + color[0]
                g = g + color[1]
                b = b + color[2]

        total_pixels = (COORDS[2] - COORDS[0]) * (COORDS[3] - COORDS[1])
        r = int(r/total_pixels)
        g = int(g/total_pixels)
        b = int(b/total_pixels)

        return (r,g,b)
        


tower = Tower()

tower.set_image()

#tower.image.show()

print(f"Top: {tower.average_color(tower.image, tower.TOP_COORDS)}")
