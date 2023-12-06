class DestinationRange():
    def __init__(self, range_text: str):
        self.destination_start, self.source_start, self.range = [int(v) for v in range_text.split()]

    def includes_seed(self, seed: int) -> int:
        if self.source_start <= seed <= self.source_start + self.range - 1:
            return True
        return False

    def calculate_destination_seed(self, seed: int) -> int:
        return seed - self.source_start + self.destination_start

class Map():
    def __init__(self, map_text: str, index: int):
        self.map_name = map_text.split(":")[0].strip()
        self.map_rank = index
        self.destination_ranges = [DestinationRange(range_text) for range_text in map_text.split(":")[1].strip().split("\n")]

    def get_destination(self, source_seed: int) -> int:
        destination_seed = source_seed
        for range in self.destination_ranges:
            if range.includes_seed(source_seed):
                destination_seed = range.calculate_destination_seed(source_seed)
                break
        return destination_seed


def part1():
    with open("2023/day5.input") as input_file:
        input = input_file.read().split("\n\n")

    maps = [Map(map_text, index) for index, map_text in enumerate(input[1:])]

    seeds = {int(seed_number): int(seed_number) for seed_numbers in input[0].split(":") if not seed_numbers.startswith("seeds")
                                    for seed_number in seed_numbers.split()}

    for source_seed in seeds.keys():
        for map in maps:
            seeds[source_seed] = map.get_destination(seeds[source_seed])

    return min(seeds.values())


def part2():
    with open("2023/day5.input") as input_file:
        input = input_file.read().split("\n\n")

    maps = [Map(map_text, index) for index, map_text in enumerate(input[1:])]


    seeds_prep = [list(range(int(seed_numbers.split()[index]), int(seed_numbers.split()[index]) + int(seed_numbers.split()[index + 1])))
                      for seed_numbers in input[0].split(":") if not seed_numbers.startswith("seeds")
                            for index, _ in enumerate(seed_numbers.split()) if index % 2 == 0]

    seeds = {int(seed): int(seed) for seeds in seeds_prep for seed in seeds}

    print(f"Number of seeds: {len(seeds)}")

    for source_seed in seeds.keys():
        for map in maps:
            seeds[source_seed] = map.get_destination(seeds[source_seed])

    return min(seeds.values())


if __name__ == "__main__":
    print(f"Part 1: {part1()}") # 600279879
    print(f"Part 2: {part2()}") # 20191102
