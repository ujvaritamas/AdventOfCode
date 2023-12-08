import re

def check(time: int, dist_to_check) ->int:
    ret = 0
    for hold_time in range(time):
        distance = hold_time * (time - hold_time)

        if distance> dist_to_check:
            ret+=1

    return ret

def parse(file_path):
    with open(file_path) as file:
        lines = file.readlines()

    time = 0
    distance = []

    for line in lines:
        tmp = ""
        for i in re.findall(r'\d+',  line):
            tmp+=i
        if "Time:" in line:
            time = int(tmp)
        else:
            distance = int(tmp)

    print(time)
    print(distance)
    ret = check(time, distance)

    print("Final result: ", ret)

def solve(file_path):
    parse(file_path)

solve("test_input.txt")