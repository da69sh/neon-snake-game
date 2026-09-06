from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
HEAD_COLOR = "#00FF41"  # Neon green
BODY_COLORS = ["#00FF41", "#00DD33", "#00BB25"]  # Gradient greens



class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for idx, position in enumerate(STARTING_POSITIONS):
            new_segment = Turtle("square")
            # Color gradient for snake body
            color = BODY_COLORS[min(idx, len(BODY_COLORS) - 1)]
            new_segment.color(color)
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def wrap_edges(self):
        x = self.head.xcor()
        y = self.head.ycor()
        if x > 280:
            self.head.goto(-280, y)
        elif x < -280:
            self.head.goto(280, y)
        elif y > 280:
            self.head.goto(x, -280)
        elif y < -280:
            self.head.goto(x, 280)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        new_segment = Turtle("square")
        # Color new segments with gradient
        num_colors = len(BODY_COLORS)
        color_idx = (len(self.segments) - 1) % num_colors
        new_segment.color(BODY_COLORS[color_idx])
        new_segment.penup()
        self.segments.append(new_segment)
        new_segment.goto(self.segments[-2].position())        
