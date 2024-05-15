import random

class Snake:
    def __init__(self, space, body):
        self.space = space
        self.body_size = body
        self.coordinates = []
        self.squares = []

        for i in range(0, body):
            self.coordinates.append([0,0])

    def go_up(self):
        self.coordinates.insert(0, (self.coordinates[0][0], self.coordinates[0][1] - self.space))

    def go_down(self):
         self.coordinates.insert(0, (self.coordinates[0][0], self.coordinates[0][1] + self.space))

    def go_left(self):
        self.coordinates.insert(0, (self.coordinates[0][0] - self.space, self.coordinates[0][1]))

    def go_right(self):
        self.coordinates.insert(0, (self.coordinates[0][0] + self.space, self.coordinates[0][1]))