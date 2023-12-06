import re


class Converter:

    def __init__(self, file_path) -> None:
        self.read_seeds = True
        self.file_path = file_path

        self.inp = []
        self.converter_ranges = [[], [], [], [], [], [], []]
        self.converter_index = -1



    def parse_seed(self, line:str):
        
        self.inp += [int(i) for i in re.findall(r'\d+',  line)]
        #self.seeds += [int(i) for i in re.findall(r'\d+',  line)]

    def convert_seed(self):
        ret = []
        for i in range(0, len(self.inp), 2):
            ret += [i for i in range(self.inp[i], self.inp[i]+self.inp[i+1])]
        self.inp = ret
    
    def parse_other(self, line:str):
        parsed = line.split()
        if len(parsed)<3:
            #skip
            return
        self.converter_ranges[self.converter_index].append([int(i) for i in parsed])



    def convert(self, inp, ranges):
        ret = 0

        is_converted = False
        for conv in ranges:
            #0 - dest range start
            #1 - source range start
            #2 range length
            if inp>=conv[1] and inp<=(conv[1]+conv[2]):
                dist_from_start = inp - conv[1]
                ret = conv[0] + dist_from_start
                is_converted = True
                break
        if not is_converted:
            ret = inp
        return ret

    def print_min(self):
        print(min(self.inp))
    
    def parse(self):
        with open(self.file_path) as file:
            lines = file.readlines()
        for line in lines:
            if line == "\n":
                self.converter_index+=1
                self.read_seeds = False
                continue

            if self.read_seeds:
                self.parse_seed(line)
            else:
                self.parse_other(line)


def solve():
    min_val = None
    converter = Converter('test_input.txt')
    converter.parse()
    #converter.print_min()
    print(converter.inp)
    print(converter.converter_ranges)

    for i in range(0, len(converter.inp), 2):
        print(converter.inp[i], converter.inp[i]+converter.inp[i+1])
        for j in range(converter.inp[i], converter.inp[i]+converter.inp[i+1]):
            print(j, converter.inp[i]+converter.inp[i+1])
            ret = j
            for conv in converter.converter_ranges:
                ret = converter.convert(ret, conv)
            if min_val== None:
                min_val = ret
            else:
                min_val = min(min_val, ret)
                
    print(min_val)


solve()