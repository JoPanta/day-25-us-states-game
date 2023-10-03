from turtle import Turtle


class WriteTheState(Turtle):

    def __init__(self, answer, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(answer, False, "center", ("Arial", 7, 'bold'))


