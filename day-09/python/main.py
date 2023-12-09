import unittest
from os import path, getcwd
import itertools
import math

instruction_map = {"L": 0, "R": 1}


def get_differences(list: list[int]) -> list[int]:
    ret_val = []
    for i in range(len(list) - 1):
        ret_val.append(list[i + 1] - list[i])
    return ret_val


def part_one(value: str) -> int:
    score: int = 0
    filePath = path.join(getcwd(), "..", "data", value)

    with open(filePath, "r") as file:
        readings = file.read().split("\n")

        for reading in readings:
            reading_split = [int(x) for x in reading.split(" ")]
            new_readings = [get_differences(reading_split)]
            while True:
                new_readings.append(get_differences(new_readings[-1]))
                if not any(x != 0 for x in new_readings[-1]):
                    break

            reversed_new_readings = list(reversed(new_readings))
            for index, values in enumerate(reversed_new_readings):
                prev_diff = reversed_new_readings[max(index - 1, 0)][-1]
                values.append(values[-1] + prev_diff)

            score += reading_split[-1] + reversed_new_readings[-1][-1]

    return score


def part_two(value: str) -> int:
    score: int = 0
    filePath = path.join(getcwd(), "..", "data", value)

    with open(filePath, "r") as file:
        readings = file.read().split("\n")

        for reading in readings:
            reading_split = [int(x) for x in reading.split(" ")]
            new_readings = [get_differences(reading_split)]
            while True:
                new_readings.append(get_differences(new_readings[-1]))
                if not any(x != 0 for x in new_readings[-1]):
                    break

            reversed_new_readings = list(reversed(new_readings))
            for index, values in enumerate(reversed_new_readings):
                if index == 0:
                    continue
                prev_diff = reversed_new_readings[index - 1][0]
                values.insert(0, values[0] - prev_diff)

            score += reading_split[0] - reversed_new_readings[-1][0]

    return score


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("test.txt"), 114)

    def test_part_one_solution(self):
        self.assertEqual(part_one("input.txt"), 1681758908)

    def test_part_two(self):
        self.assertEqual(part_two("test.txt"), 2)

    def test_part_two_solution(self):
        self.assertEqual(part_two("input.txt"), 803)


if __name__ == "__main__":
    # unittest.main()
    print(part_two("input.txt"))
