import math

class WSN:

    def __init__(self, id, pos_x, pos_y):
        self.id = id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.data =0
        self.status = None


    def dist(self, y):
        x_dist = (self.pos_x - y.pos_x)
        y_dist = (self.pos_y - y.pos_y)
        return math.sqrt(x_dist * x_dist + y_dist * y_dist)

    def __str__(self):
        return 'id:{self.id}, data: {self.data},    pos_x:{self.pos_x}, pos_y: {self.pos_y}, status: {self.status}'.format(self=self)
        


if __name__=="__main__":

    n1 = WSN(10, 1, 20, 0, 0)
    n2 = WSN(10, 2, 34, 3, 4)

    print(n1.dist(n2))
    print(n1)
    print(n2)



