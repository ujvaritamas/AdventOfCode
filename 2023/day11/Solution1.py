import itertools
class Galaxy:
    def __init__(self, x:int, y:int, num:int) -> None:
        self.x = x
        self.y = y
        self.num = num

class Solution():
    def __init__(self) -> None:
        self.matrix = []
        self.galaxies = []
        self.number_of_galaxies = 0

    def add_line(self, line:str):
        self.matrix.append([i for i in line])

    def _expand_row(self):
        row_to_expand = []
        for row in range(len(self.matrix)):
            insert_row = True
            for col in range(len(self.matrix[0])):
                if self.matrix[row][col] == "#":
                    insert_row = False
                    break
            if insert_row:
                row_to_expand.append(row)
        count = 0
        for r in row_to_expand:
            self.matrix.insert(r+count, self.matrix[r+count])
            count+=1

    def _expand_col(self):
        col_to_expand = []
        for c in range(len(self.matrix[0])):
            insert_col = True
            for r in range(len(self.matrix)):
                if self.matrix[r][c] == "#":
                    insert_col = False
                    break
            if insert_col:
                col_to_expand.append(c)
        count = 0
        for c in col_to_expand:
            for r in range(len(self.matrix)):
                self.matrix[r] = self.matrix[r][:c+1+count] + self.matrix[r][c+count:]
            count+=1

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

    @staticmethod
    def find_min_path_between_galaxies(g0:Galaxy, g1: Galaxy):
        min_path = abs(g0.x-g1.x)+abs(g0.y-g1.y)
        return min_path

    def solve_it(self):
        pairs = list(itertools.combinations(range(self.number_of_galaxies), 2))
        sum = 0
        for p0, p1 in pairs:
            print(p0, "- ", p1, Solution.find_min_path_between_galaxies(self.galaxies[p0], self.galaxies[p1]))
            sum += Solution.find_min_path_between_galaxies(self.galaxies[p0], self.galaxies[p1])
        
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

    #s.display()

    print("-----------------")
    s.expand_map()
    s.find_galaxies()

    #s.display()

    s.solve_it()


solve()