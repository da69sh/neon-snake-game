from turtle import Turtle
BORDER_COLOR = "#00FF41"



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color(BORDER_COLOR)
        self.goto(0, 250)
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(
            f"Score: {self.score}  High Score: {self.high_score}",
            align="center",
            font=("Arial", 28, "bold"),
        )
    
    def increase(self):
        self.score += 1
        self.high_score = max(self.high_score, self.score)
        self.update_score()
    
    def game_over(self):
        self.goto(0, 0)
        self.color("#FF006E")
        self.write("GAME OVER", align="center", font=("Arial", 40, "bold"))

    def reset_round(self):
        self.score = 0
        self.goto(0, 250)
        self.color(BORDER_COLOR)
        self.update_score()