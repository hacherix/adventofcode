import math

def main(part1=True):
    with open("2023/day6.input") as input_file:
        input = input_file.readlines()

    if part1:
        times = [int(time) for time in input[0].split(":")[1].split()]
        distances = [int(distance) for distance in input[1].split(":")[1].split()]
        races = dict(zip(times, distances))
    else:
        times = int(input[0].split(":")[1].replace(' ', '').strip())
        distances = int(input[1].split(":")[1].replace(' ', '').strip())
        races = {times: distances}

    result = 1
    for time_limit, distance_limit in races.items():
        race_strategies = [i * (time_limit - i) for i in range(1, time_limit)]
        winning_strategies_count = sum(1 for strategy in race_strategies if strategy > distance_limit)
        result = result * winning_strategies_count


    return result

def part2_maths():
    with open("2023/day6.input") as input_file:
        data = input_file.readlines()

    time = int(data[0][5:].replace(" ", ""))
    distance = int(data[1][9:].replace(" ", "")) + 1

    b1 = math.floor((time + math.sqrt(pow(time, 2) - 4 * distance))/2)
    b2 = math.ceil((time - math.sqrt(pow(time, 2) - 4 * distance))/2)

    return b1 - b2 + 1


if __name__ == "__main__":
    print(f"Part 1: {main(True)}")  # 1624896    # 0.02s
    print(f"Part 2: {main(False)}") # 32583852   # 3.66s
    print(f"Part 2 with maths: {part2_maths()}") # 0.02s
