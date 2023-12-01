import unittest
from os import path, getcwd
import re

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


def main(value: str) -> int:
    score = 0
    filePath = path.join(getcwd(), "data", value)
    with open(filePath, "r") as file:
        data = file.read().splitlines()
        for line in data:
            digits = [match.group(1) for match in re.finditer(pattern, line)]
            score += int(f"{mapper[digits[0]]}{mapper[digits[-1]]}")

    return score


class Test(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main("test-part-2.txt"), 281)

    def test_result(self):
        self.assertEqual(main("input.txt"), 54770)


if __name__ == "__main__":
    unittest.main()
