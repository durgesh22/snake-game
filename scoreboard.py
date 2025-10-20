from turtle import Turtle
ALIGNMENT="Center"
FONT=('Courier', 14, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(-5,280)
        self.color("white")
        self.ht()
        self.write(f"score={self.score}",move=False,align=ALIGNMENT,font=FONT)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score={self.score}", move=False,align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_score()

    def gameover(self):
        self.goto(0,0)
        self.write('GAME OVER', move=False, align=ALIGNMENT, font=FONT)







