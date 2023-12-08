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

    times = []
    distances = []

    for line in lines:
        if "Time:" in line:
            times += [int(i) for i in re.findall(r'\d+',  line)]
        else:
            distances += [int(i) for i in re.findall(r'\d+',  line)]

    print(times)
    print(distances)

    ret = 1
    for i in range(len(times)):
        ret *= check(times[i], distances[i])

    print("Final result: ", ret)

def solve(file_path):
    parse(file_path)

solve("test_input.txt")