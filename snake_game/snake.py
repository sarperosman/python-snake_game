starting_positions = [(20,0), (0,0), (-20,0)]
MOVE_DISTANCE = 20
from turtle import Turtle
DOWN = 270
UP = 90
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.all_squares = []
        self.create_snake()
        self.head = self.all_squares[0]

    def create_snake(self):
        for square_index in starting_positions:
            self.add_new_item(square_index)

    def add_new_item(self,position):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.all_squares.append(new_square)

    def extend(self):
        self.add_new_item(self.all_squares[-1].position())

    def move(self):
        for squares_num in range(len(self.all_squares) - 1, 0, -1):
            x_pos = self.all_squares[squares_num - 1].xcor()
            y_pos = self.all_squares[squares_num - 1].ycor()
            self.all_squares[squares_num].goto(x=x_pos, y=y_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
