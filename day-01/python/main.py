import unittest
from os import path, getcwd
import re


def part_one(value: str) -> int:
    score = 0
    filePath = path.join(getcwd(), "data", value)
    with open(filePath, "r") as file:
        data = file.read().splitlines()
        for line in data:
            digits = [int(digit) for digit in line if digit.isdigit()]
            print(digits)
            value = f"{digits[0]}{digits[-1]}"
            score += int(value)

    return score


def part_two(value: str) -> int:
    mapper = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    pattern = r"(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))"
    score = 0
    filePath = path.join(getcwd(), "data", value)
    with open(filePath, "r") as file:
        data = file.read().splitlines()
        for line in data:
            digits = [match.group(1) for match in re.finditer(pattern, line)]
            score += int(f"{mapper[digits[0]]}{mapper[digits[-1]]}")

    return score


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("test.txt"), 142)

    def test_part_two(self):
        self.assertEqual(part_two("test-part-2.txt"), 281)


if __name__ == "__main__":
    unittest.main()
