import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Kubic():
    def __init__(self, size):
        super(Kubic, self).__init__()
        self.size = size
        self.init()

    def init(self):
        self.field = self.load_level()
        self.entry = Point(0, 0)
        self.shuffle()
        self.isWin = False


    def load_level(self):
        f = open('field.txt', 'r')
        field = []
        for row in f:
            field.append([int(x) for x in row.strip().split(" ")])
        f.close()
        return field

    def shuffle(self):
        for i in range(100):
            random.choice([self.up, self.down, self.left, self.right, self.right_shift, self.down_shift])()

    def check_win(self):
        check_point = [[0, 0], [0, 2], [2, 0], [2, 2]]
        count = 0
        for i in range(len(check_point)):
            row = check_point[i][0]
            col = check_point[i][1]
            if self.field[row][col] == self.field[row][col+1] == self.field[row+1][col] == self.field[row+1][col+1]:
                count += 1

        #print(count)
        if count == 4:
            self.isWin = True

    def up(self):
        if self.entry.y > 0:
            self.entry.y -= 1

    def down(self):
        if self.entry.y < 3:
            self.entry.y += 1

    def right(self):
        if self.entry.x < 3:
            self.entry.x += 1

    def left(self):
        if self.entry.x > 0:
            self.entry.x -= 1

    def right_shift(self):
        self.field[self.entry.y][0], self.field[self.entry.y][1], self.field[self.entry.y][2], self.field[self.entry.y][3] = \
            self.field[self.entry.y][3], self.field[self.entry.y][0], self.field[self.entry.y][1], self.field[self.entry.y][2]
        self.check_win()

    def left_shift(self):
        self.field[self.entry.y][0], self.field[self.entry.y][1], self.field[self.entry.y][2], self.field[self.entry.y][3] = \
            self.field[self.entry.y][1], self.field[self.entry.y][2], self.field[self.entry.y][3], self.field[self.entry.y][0]
        self.check_win()

    def down_shift(self):
        self.field[0][self.entry.x], self.field[1][self.entry.x], self.field[2][self.entry.x], self.field[3][self.entry.x] = \
            self.field[3][self.entry.x], self.field[0][self.entry.x], self.field[1][self.entry.x], self.field[2][self.entry.x]
        self.check_win()

    def up_shift(self):
        self.field[0][self.entry.x], self.field[1][self.entry.x], self.field[2][self.entry.x], self.field[3][self.entry.x] = \
            self.field[1][self.entry.x], self.field[2][self.entry.x], self.field[3][self.entry.x], self.field[0][self.entry.x]
        self.check_win()


    def reset_game(self):
        self.init()

