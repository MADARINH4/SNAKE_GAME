import random

class Food: 
    def __init__(self, space, width, height):
        x = random.randint(0, (width//space)-1) * space
        y = random.randint(0, (height//space)-1) * space

        self.coordinates = [x, y]