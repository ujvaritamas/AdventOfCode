class Solution:
    def __init__(self) -> None:
        self.inp = []

    def display(self):
        for i in self.inp:
            print(i)

    def add_inp(self, inp):
        self.inp.append(inp)

    @staticmethod
    def convert(data:list):
        return [data[i+1]-data[i] for i in range(len(data)-1)]

    @staticmethod
    def check(data:list):
        for i in data:
            if i!=0:
                return False
        return True

    @staticmethod
    def calc(data:list):
        history = []
        history.append(data)
        act = data
        while not Solution.check(act):
            act = Solution.convert(act)
            history.append(act)

        print(history)


        val = 0
        for h in reversed(history):
            val = h[-1] + val

        print(val)
        return val


    def calculate(self):
        result = 0
        for i in self.inp:
            result += Solution.calc(i)

        print("Final result: ", result)



def parse(file_path:str, s:Solution):
    with open(file_path) as file:
        lines = file.readlines()

    for line in lines:
        tmp = [int(i) for i in line.rstrip().split(" ")]
        s.add_inp(tmp)

def solve():
    s = Solution()
    parse("test_input.txt", s)

    s.display()

    s.calculate()

solve()
