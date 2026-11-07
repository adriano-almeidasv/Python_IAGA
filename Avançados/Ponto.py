
class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return(self.x)

    def setX(self, x):
        self.x = x

    def getY(self):
        return(self.y)

    def setY(self, y):
        self.y = y

    def posicao(self):
        if ((self.x > 0) and (self.y > 0)):
            return("Q1")
        elif ((self.x < 0) and (self.y > 0)):
            return("Q2")
        elif ((self.x < 0) and (self.y < 0)):
            return("Q3")  
        elif ((self.x > 0) and (self.y < 0)):
            return("Q4")
        elif ((self.x != 0) and (self.y == 0)):
            return("Eixo x")
        elif ((self.x == 0) and (self.y != 0)):
            return("Eixo y")
        else:
            return("Origem")

    def __str__(self):
        return(f"(x: {self.x}, y: {self.y}) = {self.posicao()}")
