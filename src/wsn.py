import math

class WSN:

    def __init__(self, power, id, data, pos_x, pos_y):
        self.id = id
        self.power = power
        self.data = data
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rx = None


    def dist(self, y):
        x_dist = (self.pos_x - y.pos_x)
        y_dist = (self.pos_y - y.pos_y)
        return math.sqrt(x_dist * x_dist + y_dist * y_dist)

    def __str__(self):
        return 'id:{self.id}, power: {self.power}, data: {self.data}, pos_x:{self.pos_x}, pos_y: {self.pos_y}'.format(self=self)
        


if __name__=="__main__":

    n1 = WSN(10, 1, 20, 0, 0)
    n2 = WSN(10, 2, 34, 3, 4)

    print(n1.dist(n2))
    print(n1)
    print(n2)



