class place:

    def __init__(self, x1, y1, x2, y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

    def area(self):
        length = self.x2-self.x1
        breath = self.y2-self.y1
        return length*breath



if __name__=="__main__":

    c1=place(0,0, 5,5)

    print(c1.area())

