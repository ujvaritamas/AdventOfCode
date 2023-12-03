class FoundNumber:
    def __init__(self, start_index, end_index, value, line_index) -> None:
        self.start_index = start_index
        self.end_index = end_index
        self.value = value
        self.line_index = line_index

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
                return True
        return False

    def is_symbol_left(self, left_element):
        return True if is_symbol(left_element) else False

    def is_symbol_right(self, right_element):
        return True if is_symbol(right_element) else False

    def is_symbol_down(self, next_line):
        start = self.start_index - 1 if (self.start_index-1)>=0 else 0
        end = self.end_index + 1 if (self.end_index+1)<=(len(next_line) - 1) else len(next_line) - 1
        
        for i in range(start, end+1):
            if is_symbol(next_line[i]):
                return True
        return False

def is_symbol(c):
    if c=='.':
        return False
    return True

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

    ret = 0
    rr = []
    for n in found_numbers:

        print(n.__dict__, n.is_part_number(matrix))
        
        if n.is_part_number(matrix):
            rr.append(n.value)
            ret += n.value

    print(matrix)

    print(ret)



solve('test_input.txt')