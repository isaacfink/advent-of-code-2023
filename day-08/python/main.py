import unittest
from os import path, getcwd
import itertools
import math

instruction_map = {"L": 0, "R": 1}


def part_one(value: str) -> int:
    steps: int = 0
    filePath = path.join(getcwd(), "..", "data", value)

    with open(filePath, "r") as file:
        rounds = [r.split(" = ") for r in file.read().split("\n")]
        instructions = list(rounds[0][0])

        map = {}

        for pos in rounds[2::]:
            p, l, r = list(
                [
                    pos[0],
                ]
                + pos[1].replace("(", "").replace(")", "").replace(" ", "").split(","),
            )
            map[p] = [l, r]

    position = "AAA"
    while True:
        if position == "ZZZ":
            break
        move = instructions[steps % len(instructions)]
        position = map[position][instruction_map[move]]
        steps += 1

    return steps


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_of_list(numbers):
    current_lcm = numbers[0]
    for number in numbers[1:]:
        current_lcm = lcm(current_lcm, number)
    return current_lcm


def part_two(value: str) -> int:
    steps: int = 0
    filePath = path.join(getcwd(), "..", "data", value)

    map = {}
    with open(filePath, "r") as file:
        rounds = [r.split(" = ") for r in file.read().split("\n")]
        instructions = list(rounds[0][0])

        for pos in rounds[2::]:
            p, l, r = list(
                [
                    pos[0],
                ]
                + pos[1].replace("(", "").replace(")", "").replace(" ", "").split(","),
            )
            map[p] = [l, r]

    positions = list(map.keys())
    positions_starting_with_a = list(filter(lambda x: x[2] == "A", positions))

    scores = []

    positions = positions_starting_with_a

    for pos in positions:
        local_step = 0
        while True:
            if pos[2] == "Z":
                scores.append(local_step)
                break
            move = instructions[local_step % len(instructions)]
            pos = map[pos][instruction_map[move]]
            local_step += 1

    return lcm_of_list(scores)


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("test.txt"), 2)

    def test_part_one_2(self):
        self.assertEqual(part_one("test2.txt"), 6)

    def test_part_1_solution(self):
        self.assertEqual(part_one("input.txt"), 13939)

    def test_part_two(self):
        self.assertEqual(part_two("testPart2.txt"), 6)

    def test_part_two_solution(self):
        self.assertEqual(part_two("input.txt"), 8906539031197)


if __name__ == "__main__":
    unittest.main()
