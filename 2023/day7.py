def hand_strength(cards: str, joker: str):
    hand_count = {card: cards.count(card) for card in cards}
    jokers = hand_count.pop(joker, 0)
    hand_count = list(hand_count.values())
    hand_count.sort()

    if len(hand_count) > 1:
        return str(hand_count[-1] + jokers) + str(hand_count[-2])
    elif len(hand_count) == 1:
        return str(hand_count[-1] + jokers) + "0"
    else:
        return "50"

def main(card_rank: str, joker: str):
    with open("2023/day7full.input") as input_file:
        hands = input_file.readlines()

    hands_strength = [int("".join([hand_strength(hand.split()[0], joker)] +
                                  [str(card_rank.index(card)).rjust(2, "0") for card in hand.split()[0]] +
                                  [hand.split()[1].rjust(10, "0")]))
                                    for hand in hands]
    hands_strength.sort()

    return sum((index + 1) * (hand % 1000000000) for index, hand in enumerate(hands_strength))

if __name__ == "__main__":
    print(f"Part 1: {main(card_rank="23456789TJQKA", joker="")}")  # 252052080  # 0.02s
    print(f"Part 2: {main(card_rank="J23456789TQKA", joker="J")}") # 252898370  # 0.02s
