from trebuchet_part1 import SolutionPart1

class SpelledNumbers:
        NUMBERS = [
            {'str': 'one', 'value': 1},
            {'str': 'two', 'value': 2},
            {'str': 'three', 'value': 3},
            {'str': 'four', 'value': 4},
            {'str': 'five', 'value': 5},
            {'str': 'six', 'value': 6},
            {'str': 'seven', 'value': 7},
            {'str': 'eight', 'value': 8},
            {'str': 'nine', 'value': 9}]

class SolutionPart2(SolutionPart1):
    def collect_numbers(self, s:str)->int:
        is_first_digit_found = False
        first_digit = {'index': -1, 'value': 0}
        last_digit = {'index': -1, 'value': 0}
        index = 0
        #collect last and first digit
        for c in s:
            if c.isdigit():
                if not is_first_digit_found:
                    first_digit['value'] = int(c)
                    first_digit['index'] = index
                    is_first_digit_found = True

                last_digit['value'] = int(c)
                last_digit['index'] = index
            index+=1

        #handle if no digit in s
        if not is_first_digit_found:
            self.__handle_s_without_normal_digit(s, first_digit, last_digit)

        #search spelled digits before and after founded digits
        else:
            self.__handle_spelled_digits_with_normal_digits(s, first_digit, last_digit)

        return first_digit['value'] * 10 + last_digit['value']
    
    def __handle_s_without_normal_digit(self, s, first_digit, last_digit):
        first_digit['index'], first_digit['value'] =\
            self._search_before_first_digit(s, len(s))

        last_digit['index'], last_digit['value'] =\
            self.__search_after_last_digit(s, 0)

    def __handle_spelled_digits_with_normal_digits(self, s, first_digit, last_digit):
        spelled_first_digit_index, spelled_first_digit = \
            self._search_before_first_digit(s, first_digit['index'])
        spelled_last_digit_index, spelled_last_digit = \
            self.__search_after_last_digit(s, last_digit['index'])

        if first_digit['index']> spelled_first_digit_index:
            first_digit['index']= spelled_first_digit_index
            first_digit['value']= spelled_first_digit

        if last_digit['index']< spelled_last_digit_index:
            last_digit['index']= spelled_last_digit_index
            last_digit['value']= spelled_last_digit

    def _search_before_first_digit(self, s, index_of_first_digit):
        index = None
        value = -1
        for num in SpelledNumbers.NUMBERS:
            found_at = self.__find_spelled_number(num['str'], s[:index_of_first_digit].find)
            if found_at>-1:
                    if index == None or index > found_at:
                        index = found_at
                        value = num['value']
        index = index_of_first_digit if index == None else index
        return (index, value)

    def __search_after_last_digit(self, s, index_of_last_digit):
        index = None
        value = -1
        for num in SpelledNumbers.NUMBERS:
            found_at = self.__find_spelled_number(num['str'], s[index_of_last_digit:].rfind)
            if found_at>-1:
                    if index == None or index < found_at:
                        index = found_at
                        value = num['value']
        index = index_of_last_digit if index == None else index+index_of_last_digit
        return (index, value)

    #strategy
    def __find_spelled_number(self, spelled_number, strategy):
        result = strategy(spelled_number)

        return result

if __name__ == "__main__":
    solve = SolutionPart2()
    print(solve.decode('test_input.txt'))



