def get_card_matches():
    with open("2023/day4.input") as input_file:
        input = input_file.readlines()

    return [len(set(number_set.split("|")[0].split()) & set(number_set.split("|")[1].split()))
                         for card in input
                               for number_set in card.split(":") if not number_set.startswith("Card")]


def part1():
    card_matches = get_card_matches()

    return sum([2 ** (match_number - 1) for match_number in card_matches if match_number > 0])


def part2():
    card_matches = get_card_matches()

    cards_amount = len(card_matches)
    cards_count = [1] * cards_amount

    for card_index, card in enumerate(card_matches):
        for next_card_index in range(card_index + 1, card_index + card + 1):
            if next_card_index < cards_amount:
                cards_count[next_card_index] += 1 * cards_count[card_index]

    return sum(cards_count)

if __name__ == "__main__":
    print(f"Part 1: {part1()}") # 21821
    print(f"Part 2: {part2()}") # 5539496
