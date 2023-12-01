import unittest
from os import path, getcwd


def main(value: str) -> int:
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


class Test(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main("test.txt"), 142)


if __name__ == "__main__":
    unittest.main()
