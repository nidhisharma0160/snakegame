from turtle import Turtle
ALIGNMENT = "CENTER"
FONT = ("Arial", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.penup()
        self.goto(0,270)
        self.write(f"Score = {self.score} ",align= ALIGNMENT, font = FONT  )
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} Highscore = {self.highscore}", align= ALIGNMENT, font = FONT)

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = str(self.score)
            with open("data.txt", mode="w") as file:
                file.write(self.highscore)
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.update_score()



    #def game_over(self):
    #   self.goto(0,0)
    #  self.write("GAME OVER", align = ALIGNMENT, font= FONT)
