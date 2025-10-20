from turtle import Turtle
ALIGNMENT="Center"
FONT=('Courier', 14, 'normal')
class Gameover(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.write("GameOver!!!",move=False,align=ALIGNMENT,font=FONT)








