def part1():
    with open("2023/day3.input") as input_file:
        input = input_file.read()

    schema_parsed = [[value for value in row] for row in input.split()]
    height = len(schema_parsed)
    width = len(schema_parsed[0])

    result = 0
    number = ""
    has_adjacent_symbol = False

    for y, row in enumerate(schema_parsed):
        for x, value in enumerate(row):
            if value in "0123456789":
                number = number + value
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if j + y < height and i + x < width:
                            if schema_parsed[y + j][x + i] not in ".0123456789":
                                has_adjacent_symbol = True
            elif number != "":
                if has_adjacent_symbol:
                    result += int(number)
                number = ""
                has_adjacent_symbol = False
        if number != "":
            if has_adjacent_symbol:
                result += int(number)
            number = ""
            has_adjacent_symbol = False

    return result

def part2():
    with open("2023/day3.input") as input_file:
        input = input_file.read()

    schema_parsed = [[value for value in row] for row in input.split()]
    height = len(schema_parsed)
    width = len(schema_parsed[0])

    result = {}
    number = ""
    adjacent_symbol = ()

    for y, row in enumerate(schema_parsed):
        for x, value in enumerate(row):
            if value in "0123456789":
                number = number + value
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if j + y < height and i + x < width:
                            if schema_parsed[y + j][x + i] == "*":
                                adjacent_symbol = (y + j, x + i)
            elif number != "":
                if adjacent_symbol != ():
                    if adjacent_symbol in result:
                        result[adjacent_symbol] = result[adjacent_symbol] + [int(number)]
                    else:
                        result[adjacent_symbol] = [int(number)]
                number = ""
                adjacent_symbol = ()
        if number != "":
            if adjacent_symbol != ():
                if adjacent_symbol in result:
                    result[adjacent_symbol] = result[adjacent_symbol] + [int(number)]
                else:
                    result[adjacent_symbol] = [int(number)]
            number = ""
            adjacent_symbol = ()

    return sum([value[0] * value[1] for key, value in result.items() if len(result[key]) == 2])

if __name__ == "__main__":
    print(f"Part 1: {part1()}") # 527369
    print(f"Part 2: {part2()}") # 73074886
