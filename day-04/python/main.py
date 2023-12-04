import unittest
from os import path, getcwd


def part_one(value: str) -> int:
    score = 0

    filePath = path.join(getcwd(), "..", "data", value)

    def filter_empty(x):
        return x != ""

    with open(filePath, "r") as file:
        cards = file.readlines()

        for card in cards:
            card_score = 0
            [_, numbers] = card.split(":")
            [winning_numbers, playing_numbers] = numbers.split("|")
            winning_numbers = [x.strip() for x in winning_numbers.strip().split()]
            playing_numbers = [x.strip() for x in playing_numbers.strip().split()]

            for number in winning_numbers:
                if number in playing_numbers:
                    card_score = card_score * 2 if card_score > 0 else 1

            score = score + card_score

    return score


class Cards:
    winning: list[int]
    playing: list[int]
    copies: int


def part_two(value: str) -> int:
    filePath = path.join(getcwd(), "..", "data", value)
    with open(filePath, "r") as file:
        cards: list[Cards] = []
        lines = file.readlines()
        for line in lines:
            card = Cards()
            [_, numbers] = line.split(":")
            [winning_numbers, playing_numbers] = numbers.split("|")
            winning_numbers = [int(x.strip()) for x in winning_numbers.strip().split()]
            playing_numbers = [int(x.strip()) for x in playing_numbers.strip().split()]
            card.winning = winning_numbers
            card.playing = playing_numbers
            card.copies = 1
            cards.append(card)

        for index, card in enumerate(cards):
            score = 0
            for number in card.winning:
                if number in card.playing:
                    score += 1

            for i in range(index + 1, min(index + score + 1, len(cards) - 1)):
                cards[i].copies += card.copies

    return sum([card.copies for card in cards])


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("test.txt"), 13)

    def test_part_1_solution(self):
        self.assertEqual(part_one("input.txt"), 28538)

    def test_part_two(self):
        self.assertEqual(part_two("test.txt"), 30)

    def test_part_two_solution(self):
        self.assertEqual(part_two("input.txt"), 9425061)


if __name__ == "__main__":
    unittest.main()
