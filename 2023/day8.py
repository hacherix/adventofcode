import math

def main(starting_location, end_location):
    with open("2023/day8full.input") as input_file:
        input = input_file.read()

    instructions = [int(instruction == "R") for instruction in input.split("\n")[0]]
    instructions_length = len(instructions)

    locations = {location.split("=")[0].strip(): [next_location.strip("( )") for next_location in location.split("=")[1].split(",")]
                        for location in input.split("\n")[2:] if len(location) > 0}

    start_locations = [location for location in locations if location[::-1].startswith(starting_location)]

    location_steps = []
    for start_location in start_locations:
        steps = 0
        current_location = start_location
        while not current_location[::-1].startswith(end_location):
            instructions_steps = 0
            while not current_location[::-1].startswith(end_location) and instructions_steps < instructions_length:
                current_location = locations[current_location][instructions[instructions_steps]]
                steps += 1
                instructions_steps += 1
        location_steps.append(steps)

    return location_steps

if __name__ == "__main__":
    print(f"Part 1: {main(starting_location="AAA", end_location="ZZZ")}")        # 20777          # 0.02s
    print(f"Part 2: {math.lcm(*main(starting_location="A", end_location="Z"))}") # 13289612809129 # 0.02s
