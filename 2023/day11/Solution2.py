import itertools
class Galaxy:
    def __init__(self, x:int, y:int, num:int) -> None:
        self.x = x
        self.y = y
        self.num = num

class Solution():
    EXPAND_NUMBER = 1000000
    def __init__(self) -> None:
        self.matrix = []
        self.galaxies = []
        self.number_of_galaxies = 0

        self.row_to_expand = []
        self.col_to_expand = []

    def add_line(self, line:str):
        self.matrix.append([i for i in line])

    def _expand_row(self):
        for row in range(len(self.matrix)):
            insert_row = True
            for col in range(len(self.matrix[0])):
                if self.matrix[row][col] == "#":
                    insert_row = False
                    break
            if insert_row:
                self.row_to_expand.append(row)

    def _expand_col(self):
        for c in range(len(self.matrix[0])):
            insert_col = True
            for r in range(len(self.matrix)):
                if self.matrix[r][c] == "#":
                    insert_col = False
                    break
            if insert_col:
                self.col_to_expand.append(c)

    def expand_map(self):
        self._expand_row()
        self._expand_col()

    def find_galaxies(self):
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[0])):
                if self.matrix[r][c] == "#":
                    g = Galaxy(c, r, self.number_of_galaxies)
                    self.matrix[r][c] = self.number_of_galaxies
                    self.galaxies.append(g)
                    self.number_of_galaxies+=1

    def find_min_path_between_galaxies(self, g0:Galaxy, g1: Galaxy):
        min_path = abs(g0.x-g1.x)+abs(g0.y-g1.y)

        for c in self.col_to_expand:
            if g0.x >= g1.x:
                if g1.x<=c and c<=g0.x:
                    min_path += Solution.EXPAND_NUMBER -1
            else:
                if g0.x<=c and c<=g1.x:
                    min_path += Solution.EXPAND_NUMBER -1

        for r in self.row_to_expand:
            if g0.y >= g1.y:
                if g1.y<=r and r<=g0.y:
                    min_path += Solution.EXPAND_NUMBER -1
            else:
                if g0.y<=r and r<=g1.y:
                    min_path += Solution.EXPAND_NUMBER -1


        return min_path

    def solve_it(self):

        pairs = list(itertools.combinations(range(self.number_of_galaxies), 2))
        sum = 0
        for p0, p1 in pairs:
            print(p0, "- ", p1, self.find_min_path_between_galaxies(self.galaxies[p0], self.galaxies[p1]))
            sum += self.find_min_path_between_galaxies(self.galaxies[p0], self.galaxies[p1])
        
        print("Final result: ", sum)
    
    def display(self):
        for row in range(len(self.matrix)):
            print(self.matrix[row])


def parse(file_path:str, s:Solution):
    with open(file_path) as file:
        lines = file.readlines()

    for line in lines:
        s.add_line(line.rstrip())

def solve():
    s = Solution()
    parse("test_input.txt", s)

    s.display()

    print("-----------------")
    s.expand_map()
    s.find_galaxies()

    #s.display()

    
    s.solve_it()


solve()