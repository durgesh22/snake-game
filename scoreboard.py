from turtle import Turtle
ALIGNMENT="Center"
FONT=('Courier', 14, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.high_score=data.read()
        self.goto(-5,280)
        self.color("white")
        self.ht()
        self.write(f"score={self.score}",move=False,align=ALIGNMENT,font=FONT)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score={self.score} high_score={self.high_score}", move=False,align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_score()

    def gameover(self):
        self.goto(0,0)
        self.write('GAME OVER', move=False, align=ALIGNMENT, font=FONT)
        self.set_high_score()

    def set_high_score(self):
        if int(self.score) > int(self.high_score):
            self.high_score=self.score
        with open("data.txt",mode="w") as data:
            data.write(f"{self.high_score}")








