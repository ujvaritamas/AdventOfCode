class FoundNumber:
    def __init__(self, start_index, end_index, value, line_index) -> None:
        self.start_index = start_index
        self.end_index = end_index
        self.value = value
        self.line_index = line_index
        self.stair_position_line = None
        self.stair_position_index = None

    def is_part_number(self, matrix):
        ret = False

        if self.line_index > 0:
            ret = ret or self.is_symbol_up(matrix[self.line_index - 1])

        if self.start_index > 0:
            ret = ret or self.is_symbol_left(matrix[self.line_index][self.start_index - 1])

        if self.end_index < len(matrix[self.line_index])-1:
            ret = ret or self.is_symbol_right(matrix[self.line_index][self.end_index + 1])

        if self.line_index < len(matrix) - 1:
            ret = ret or self.is_symbol_down(matrix[self.line_index + 1])

        return ret

    def is_symbol_up(self, prev_line):
        start = self.start_index - 1 if (self.start_index-1)>=0 else 0
        end = self.end_index + 1 if (self.end_index+1)<=(len(prev_line) - 1) else len(prev_line) - 1

        for i in range(start, end+1):
            if is_symbol(prev_line[i]):
                self.stair_position_index = i
                self.stair_position_line = self.line_index - 1
                return True
        return False

    def is_symbol_left(self, left_element):
        if is_symbol(left_element):
            self.stair_position_index = self.start_index - 1
            self.stair_position_line = self.line_index
            return True
        return False

    def is_symbol_right(self, right_element):
        if is_symbol(right_element):
            self.stair_position_index = self.end_index + 1
            self.stair_position_line = self.line_index
            return True
        return False

    def is_symbol_down(self, next_line):
        start = self.start_index - 1 if (self.start_index-1)>=0 else 0
        end = self.end_index + 1 if (self.end_index+1)<=(len(next_line) - 1) else len(next_line) - 1

        for i in range(start, end+1):
            if is_symbol(next_line[i]):
                self.stair_position_index = i
                self.stair_position_line = self.line_index + 1
                return True
        return False

def is_symbol(c):
    #count only the * as symbol
    if c=='*':
        return True
    return False

class GearCollector:
    def __init__(self) -> None:
        self.gear = {}

    def add_gear(self, id, gear):
        if id not in self.gear.keys():
            self.gear[id] = (gear, False)
        else:
            self.gear[id] = (self.gear[id][0]*gear, True)

    def sum(self):
        ret = 0
        for id in self.gear:
            if self.gear[id][1]:
                ret += self.gear[id][0]
        return ret

    def print(self):
        print(self.gear)


def solve(file_path):
    matrix = []
    line_count = 0

    found_numbers = []

    with open(file_path) as file:
        lines = file.readlines()
    for line in lines:
        matrix_row = []
        start_index = None
        end_index = None
        index = 0
        value = 0
        for c in line:
            if c == '\n':
                if start_index != None:
                    number = FoundNumber(start_index, end_index, value, line_count)
                    found_numbers.append(number)

                    start_index = None
                    end_index = None
                    value = 0
                continue
            matrix_row.append(c)
            if c.isdigit():
                if start_index == None:
                    start_index = index
                end_index = index
                value = value * 10 + int(c)
            else:
                if start_index != None:
                    number = FoundNumber(start_index, end_index, value, line_count)
                    found_numbers.append(number)

                    start_index = None
                    end_index = None
                    value = 0
            index+=1
        matrix.append(matrix_row)
        line_count+=1

    collector = GearCollector()

    for n in found_numbers:

        print(n.__dict__, n.is_part_number(matrix))

        if n.is_part_number(matrix):
            id = str(n.stair_position_line) + "_"+str(n.stair_position_index)
            collector.add_gear(id, n.value)


    collector.print()
    print(collector.sum())


solve('test_input.txt')