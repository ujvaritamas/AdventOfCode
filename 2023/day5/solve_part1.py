import re


class Solver:

    def __init__(self, file_path) -> None:
        self.read_seeds = True
        self.file_path = file_path

        self.inp = []
        self.converter_ranges = []


    def parse_seed(self, line:str):
        self.inp += [int(i) for i in re.findall(r'\d+',  line)]
        #self.seeds += [int(i) for i in re.findall(r'\d+',  line)]
    
    def parse_other(self, line:str):
        parsed = line.split()
        if len(parsed)<3:
            #skip
            return
        self.converter_ranges.append([int(i) for i in parsed])



    def convert(self):
        print("input: ", self.inp)
        print("converter input: ", self.converter_ranges)
        ret = []

        for inp in self.inp:
            is_converted = False
            for conv in self.converter_ranges:
                #0 - dest range start
                #1 - source range start
                #2 range length
                if inp>=conv[1] and inp<=(conv[1]+conv[2]):
                    dist_from_start = inp - conv[1]
                    ret.append(conv[0] + dist_from_start)
                    is_converted = True
                    break
            if not is_converted:
                ret.append(inp)
        print("convert result: ", ret)
        self.inp = ret

    def print_min(self):
        print(min(self.inp))
    
    def parse(self):
        with open(self.file_path) as file:
            lines = file.readlines()

        for line in lines:
            if line == "\n":
                self.convert()
                self.read_seeds = False
                self.converter_ranges= []
                continue

            if self.read_seeds:
                self.parse_seed(line)
            else:
                self.parse_other(line)

        #last convert humidity to location
        self.convert()


def solve():
    p = Solver('test_input.txt')
    p.parse()
    p.print_min()

solve()