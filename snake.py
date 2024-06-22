import time
from turtle import Turtle


# creating the snake class

class Snake:
    def __init__(self):

        self.segment = []  # An list for each segment of the snake
        self.create()  # creating the segments of the snake
        self.head = self.segment[0]  # for repeated usage for the head of the snake through the rest of the code

    def create(self):

        for num in range(3):
            square = Turtle("square")
            square.penup()
            square.color("white")
            x = -(num * 20)
            square.setposition(x, 0)
            self.segment.append(square)

    def move(self):
        # making a link for the segment to act like one
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            # heading = self.segment[seg_num - 1].heading()
            self.segment[seg_num].setpos(new_x, new_y)
            # self.segment[seg_num].setheading(heading)
            # now each segment is shifted towards the next on for  the tail of the snake to the head
        # head is the only moving segment and the rest of the segments is following it
        self.segment[0].forward(20)

    def grow(self):
        # creating a new segment and set its position to the last segment of the snake and appending it to segments
        square = Turtle("square")
        square.penup()
        square.setpos(self.segment[-1].position())
        square.color("white")
        self.segment.append(square)
    # key movements of the snake

    def up(self):
        if self.head.heading() != 270:
            self.segment[0].setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.segment[0].setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.segment[0].setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.segment[0].setheading(0)
    def Reset(self):
        for segment in self.segment:
            segment.hideturtle()
        self.segments = []
        self.create()


