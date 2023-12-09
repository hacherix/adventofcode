def main():
    with open("2023/day9full.input") as input_file:
        inputs = input_file.readlines()

    inputs = [[int(value) for value in input.split()] for input in inputs]

    part1, part2 = [], []
    for input in inputs:
        series = [input]
        while any(value != 0 for value in series[-1]):
            series.append([value - series[-1][index] for index, value in enumerate(series[-1][1:])])
        part1.append(sum(serie[-1] for serie in series))
        part2.append(sum(serie[0] for index, serie in enumerate(series) if index % 2 == 0)
                     - sum(serie[0] for index, serie in enumerate(series) if index % 2 == 1))

    return sum(part1), sum(part2)

if __name__ == "__main__":
    print(f"Part 1 and 2: {main()}")  # 2174807968 and 1208 # 0.0s
