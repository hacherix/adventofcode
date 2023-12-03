CUBES_LIMIT_AMOUNT = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


class Draw:
    def __init__(self, draw_text: str):
        self.color = draw_text.split()[1]
        self.amount = int(draw_text.split()[0])

    def is_draw_impossible(self) -> bool:
        return self.amount > CUBES_LIMIT_AMOUNT[self.color]


class Game:
    def __init__(self, game_text: str):
        self.number = int(game_text.split(":")[0].split()[1])
        self.draws = [Draw(draw) for hand in game_text.split(":")[1].split(";") for draw in hand.split(",")]

    def is_game_possible(self) -> bool:
        return sum([draw.is_draw_impossible() for draw in self.draws]) == 0

    def get_max_required_cubes(self, color: str) -> int:
        return max([draw.amount for draw in self.draws if draw.color == color])

    def get_power_of_set_of_cubes(self) -> int:
        result = 1
        for color in CUBES_LIMIT_AMOUNT.keys():
             result = result * max([draw.amount for draw in self.draws if draw.color == color])
        return result


def get_games() -> list[Game]:
    with open("2023/day2.input") as input_file:
        input =  input_file.readlines()
    return [Game(game.lower()) for game in input]


def part1():
    games = get_games()
    return sum([game.number for game in games if game.is_game_possible()])


def part2():
    games = get_games()
    return sum([game.get_power_of_set_of_cubes() for game in games])


if __name__ == "__main__":
    print(f"Part 1: {part1()}") # 2162
    print(f"Part 2: {part2()}") # 72513
