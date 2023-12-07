import unittest
from os import path, getcwd
import itertools

hand_scores = {
    "A": "13",
    "K": "12",
    "Q": "11",
    "J": "10",
    "T": "09",
    "9": "08",
    "8": "07",
    "7": "06",
    "6": "05",
    "5": "04",
    "4": "03",
    "3": "02",
    "2": "01",
    "*": "00",
}

hands = list(hand_scores.keys())

hand_types_scores = {
    "five_of_a_kind": "7",
    "four_of_a_kind": "6",
    "full_house": "5",
    "three_of_a_kind": "4",
    "two_pairs": "3",
    "two_of_a_kind": "2",
    "distinct": "1",
}

hand_types = list(hand_types_scores.keys())


def get_hand_type(hl: list[str]) -> str:
    matches = []
    distinct = set(hl)
    for h in distinct:
        matches.append(hl.count(h))

    if matches.count(5) == 1:
        return hand_types[0]
    elif matches.count(4) == 1:
        return hand_types[1]
    elif matches.count(3) == 1 and matches.count(2) == 1:
        return hand_types[2]
    elif matches.count(3) == 1:
        return hand_types[3]
    elif matches.count(2) == 2:
        return hand_types[4]
    elif matches.count(2) == 1:
        return hand_types[5]
    else:
        return hand_types[6]


def get_score_for_hand(hand: str, original_hand: str) -> int:
    h = [hand[i] for i in range(0, len(hand))]
    oh = [original_hand[i] for i in range(0, len(original_hand))]
    fs = hand_types_scores[get_hand_type(h)]
    for i in range(0, len(oh)):
        fs += hand_scores[oh[i]]

    return int(fs)


def get_joker_replacements(hand: str) -> list[list[str]]:
    # Identify the positions of the jokers
    joker_positions = [pos for pos, char in enumerate(hand) if char == "J"]

    # Generate all possible combinations of replacements for the jokers
    possible_replacements = []
    for replacement in itertools.product(hands, repeat=len(joker_positions)):
        new_hand = list(hand)
        for pos, rep in zip(joker_positions, replacement):
            new_hand[pos] = rep
        possible_replacements.append(["".join(new_hand), hand.replace("J", "*")])

    return possible_replacements


def get_highest_score(hands: list[list[str]]) -> int:
    highest_score = 0
    for hand in hands:
        score = get_score_for_hand(hand[0], hand[1])
        if score > highest_score:
            highest_score = score

    return highest_score


def part_one(value: str) -> int:
    score = 0
    filePath = path.join(getcwd(), "..", "data", value)

    with open(filePath, "r") as file:
        rounds = [r.split(" ") for r in file.read().split("\n")]
        sorted_rounds = sorted(rounds, key=lambda x: get_score_for_hand(x[0], x[0]))

        for index, r in enumerate(sorted_rounds):
            score += (index + 1) * int(r[1])

    return score


def part_two(value: str) -> int:
    score = 0
    filePath = path.join(getcwd(), "..", "data", value)

    with open(filePath, "r") as file:
        rounds = [r.split(" ") for r in file.read().split("\n")]
        sorted_rounds = sorted(
            rounds, key=lambda x: get_highest_score(get_joker_replacements(x[0]))
        )

        for index, r in enumerate(sorted_rounds):
            score += (index + 1) * int(r[1])

    return score


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("test.txt"), 6440)

    def test_part_1_solution(self):
        self.assertEqual(part_one("input.txt"), 250898830)

    def test_part_two(self):
        self.assertEqual(part_two("test.txt"), 5905)

    def test_part_two_solution(self):
        self.assertEqual(part_two("input.txt"), 252127335)


if __name__ == "__main__":
    unittest.main()
