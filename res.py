"""Module containing all materials"""


class Ball:
    # Initial definition
    def __init__(self, canvas, **kwargs):
        self.canvas = canvas
        self.radius = kwargs.get('radius')
        self.pos_x = kwargs.get('pos_x')
        self.pos_y = kwargs.get('pos_y')
        self.colour = kwargs.get('colour', 'red')
        self.mass = kwargs.get('mass')
        self.type = 'object'

        self.create()

    # Creates the ball
    def create(self):
        self.ball = self.canvas.create_oval(self.pos_x, self.pos_y, self.pos_x + self.radius * 2, self.pos_y + self.radius * 2)
        self.canvas.itemconfig(self.ball, fill=self.colour)

    # Moves the ball
    def move(self, x, y):
        self.canvas.delete(self.ball)

        self.pos_x = x
        self.pos_y = y

        self.create()

    # Returns the ball's coordinates
    def pos(self):
        return self.pos_x, self.pos_y, self.pos_x + self.radius * 2, self.pos_y + self.radius * 2

    forces = []         # List storing all the forces


class Container:
    # Initial definition
    def __init__(self, canvas, **kwargs):
        self.canvas = canvas
        self.width = kwargs.get('width')
        self.height = kwargs.get('height')
        self.pos_x = kwargs.get('pos_x')
        self.pos_y = kwargs.get('pos_y')
        self.type = 'boundary'

    # Returns the position of the ball
    def pos(self):
        x1 = self.pos_x
        x2 = self.pos_x + self.width
        y1 = self.pos_y
        y2 = self.pos_y + self.height

        return x1, y1, x2, y2

objects, boundaries = [], []
