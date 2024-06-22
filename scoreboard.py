from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, highestscore):
        # inheriting the Turtle object from the turtle
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = -1
        self.highestscore = highestscore 
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"score:{self.score}     highest score: {self.highestscore}", False, "center", ("arial", 20, "bold"))

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", False, "center", ("arial", 20, "bold"))
        if self.highestscore < self.score:
            self.highestscore = self.score
            self.score = 0
            self.clear()
    def get_highest_score(self):
        return self.highestscore if self.highestscore > self.score else self.score
        







