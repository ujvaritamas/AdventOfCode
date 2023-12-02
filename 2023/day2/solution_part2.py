import re

NUMBER_REGEXP_PATTERN = re.compile(r'[0-9]+')
PATTER_RED = re.compile(r'(\d+) red')
PATTER_GREEN = re.compile(r'(\d+) green')
PATTER_BLUE = re.compile(r'(\d+) blue')



def calculate_power(game_sets):
    power = 0

    red_list = []
    green_list = []
    blue_list = []

    for game_set in game_sets:

        tmp_red = PATTER_RED.findall(game_set)
        tmp_green = PATTER_GREEN.findall(game_set)
        tmp_blue = PATTER_BLUE.findall(game_set)

        number_of_red_cube = 0 if len(tmp_red) == 0 else int(tmp_red[0])
        number_of_green_cube = 0 if len(tmp_green) == 0 else int(tmp_green[0])
        number_of_blue_cube = 0 if len(tmp_blue) == 0 else int(tmp_blue[0])
        red_list.append(number_of_red_cube)
        green_list.append(number_of_green_cube)
        blue_list.append(number_of_blue_cube)
    return max(red_list) * max(green_list) * max(blue_list)

def solve(file_path):
    ret = 0
    lines = []
    with open(file_path) as file:
        lines = file.readlines()

    for line in lines:
        splitted_line = line.split(':')
        index = int(NUMBER_REGEXP_PATTERN.findall(splitted_line[0])[0])
        game_sets = splitted_line[1].split(';')

        ret += calculate_power(game_sets)
    return ret

print(solve('test_input.txt'))