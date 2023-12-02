class SolutionPart1:
    def collect_numbers(self, s:str)->int:
        is_first_digit_found = False
        first_digit = 0
        last_digit = 0
        for c in s:
            if c.isdigit():
                if not is_first_digit_found:
                    first_digit = int(c)
                    is_first_digit_found = True
                last_digit = int(c)
        return first_digit * 10 + last_digit

    def decode(self, filepath):
        ret = 0

        lines = []
        with open(filepath) as file:
            lines = file.readlines()

        for line in lines:
            ret += self.collect_numbers(line)

        return ret


if __name__ == "__main__":
    solve = SolutionPart1()
    print(solve.decode('test_input.txt'))
