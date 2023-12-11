import copy

# | up down
#- left right
#L up right
#J up left
#7 down left
#F down right
#. is ground; there is no pipe in this tile.
#S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Position:
    def __init__(self) -> None:
        self.row = 0
        self.col = 0
        self.char = ""
        self.count = 0
        self.prev_direction = None

    def set_pos(self, r:int, c:int, char:str):
        self.row = r
        self.col = c
        self.char = ""+char

    def display(self):
        print("Position (row, col): ", self.row, self.col, " char: ", self.char)

    def go(self, matrix:list, direction:Direction) ->bool:
        ret = False

        if direction == None:
            return False

        if direction == Direction.UP:
            if self.row != 0:
                self.row -= 1
                ret = True

        if direction == Direction.DOWN:
            if self.row != len(matrix):
                self.row += 1
                ret = True

        if direction == Direction.LEFT:
            if self.col != 0:
                self.col -= 1
                ret = True

        if direction == Direction.RIGHT:
            if self.col != len(matrix[0]):
                self.col += 1
                ret = True

        #update matrix
        if ret:

            if isinstance(matrix[self.row][self.col], int):
                print("We reached this alread")
                return False
            self.char = matrix[self.row][self.col]
            self.prev_direction = direction
            self.count+=1
            matrix[self.row][self.col] = self.count

        return ret




class Solution:
    def __init__(self) -> None:
        self.matrix = []
        self.pos0 = Position()
        self.pos1 = Position()
        self.number_of_row = 0
        self.number_of_col = 0

    def add_line(self, line:str):
        self.matrix.append([i for i in line])


    def display(self):
        for row in range(len(self.matrix)):
            print(self.matrix[row])

    @staticmethod
    def display_matrix(matrix):
        for row in range(len(matrix)):
            print(matrix[row])


    def find_start(self):
        self.number_of_row = len(self.matrix)
        self.number_of_col = len(self.matrix[0])

        for row in range(self.number_of_row):
            for col in range(self.number_of_col):
                if self.matrix[row][col] == "S":
                    self.pos0.set_pos(row, col, self.matrix[row][col])
                    self.pos1.set_pos(row, col, self.matrix[row][col])
                    return

    def is_connect(self, direction:Direction, char:str):
        if direction == Direction.UP:
            if char not in [".", "-", "L", "J"]:
                return True

        if direction == Direction.DOWN:
            if char not in [".", "-", "7", "F"]:
                return True

        if direction == Direction.LEFT:
            if char not in [".", "|", "J", "7"]:
                return True

        if direction == Direction.RIGHT:
            if char not in [".", "|", "L", "F"]:
                return True
        return False


    def find_directions_start(self)->list:
        ret = []
        c = self.matrix[self.pos0.row][self.pos0.col]

        #check up
        pos_row = self.pos0.row-1
        pos_col = self.pos0.col
        if pos_row>=0:
            c = self.matrix[pos_row][pos_col]
            direction = Direction.UP
            if self.is_connect(direction, c):
                ret.append(direction)

        #check down
        pos_row = self.pos0.row+1
        pos_col = self.pos0.col
        if pos_row<len(self.matrix):
            c = self.matrix[pos_row][pos_col]
            direction = Direction.DOWN
            if self.is_connect(direction, c):
                ret.append(direction)


        #check left
        pos_row = self.pos0.row
        pos_col = self.pos0.col-1
        if pos_col>=0:
            c = self.matrix[pos_row][pos_col]
            direction = Direction.LEFT
            if self.is_connect(direction, c):
                ret.append(direction)

        #check right
        pos_row = self.pos0.row
        pos_col = self.pos0.col+1
        if pos_col<len(self.matrix[0]):
            c = self.matrix[pos_row][pos_col]
            direction = Direction.RIGHT
            if self.is_connect(direction, c):
                ret.append(direction)

        return ret


# | up down
#- left right
#L up right
#J up left
#7 down left
#F down right
#. is ground; there is no pipe in this tile.
#S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

    def find_next_direction(self, pos:Position)->Direction:
        c = self.matrix[pos.row][pos.col]

        if pos.prev_direction == Direction.UP:
            if c == "|":
                return Direction.UP
            elif c== "F":
                return Direction.RIGHT
            elif c=="7":
                return Direction.LEFT

        if pos.prev_direction == Direction.DOWN:
            if c == "|":
                return Direction.DOWN
            elif c== "L":
                return Direction.RIGHT
            elif c=="J":
                return Direction.LEFT

        if pos.prev_direction == Direction.LEFT:
            if c == "-":
                return Direction.LEFT
            elif c== "F":
                return Direction.DOWN
            elif c=="L":
                return Direction.UP

        if pos.prev_direction == Direction.RIGHT:
            if c == "-":
                return Direction.RIGHT
            elif c== "7":
                return Direction.DOWN
            elif c=="J":
                return Direction.UP
        return None


    def is_finish(self, matrix):
        if self.pos0.row == self.pos1.row and self.pos0.col == self.pos1.col:
            return True

    def solve_it(self):
        matrix_copy = copy.deepcopy(self.matrix)
        self.find_start()

        #mark the start with 0
        matrix_copy[self.pos0.row][self.pos0.col] = 0

        tmp_dirs = self.find_directions_start()

        #including S, which will have exactly two pipes connecting to it
        assert len(tmp_dirs) == 2
        print(tmp_dirs)


        self.pos0.go(matrix_copy, tmp_dirs[0])
        self.pos1.go(matrix_copy, tmp_dirs[1])

        Solution.display_matrix(matrix_copy)

        self.pos0.display()
        self.pos1.display()

        fin = False
        while(not fin):
            tmp_dirs[0]= self.find_next_direction(self.pos0)
            tmp_dirs[1] = self.find_next_direction(self.pos1)


            if(tmp_dirs[0] == None and tmp_dirs[1] == None):
                print("No more direction")
                return
            g0 = self.pos0.go(matrix_copy, tmp_dirs[0])
            g1= self.pos1.go(matrix_copy, tmp_dirs[1])

            print("rrr", g0, g1)

            if not (g0 or g1):
                return

            #Solution.display_matrix(matrix_copy)

            self.pos0.display()
            self.pos1.display()

            if self.is_finish(matrix_copy):
                fin = True


def parse(file_path:str, s:Solution):
    with open(file_path) as file:
        lines = file.readlines()

    for line in lines:
        s.add_line(line.rstrip())



def solve():
    s = Solution()
    parse("test_input.txt", s)

    s.display()
    s.solve_it()

    print("Final result: ", max(s.pos0.count, s.pos1.count))

solve()