import unittest
from os import path, getcwd


def part_one(value: str) -> int:
    score = 0
    filePath = path.join(getcwd(), "..", "data", value)

    with open(filePath, "r") as file:
        rounds = file.readlines()
        time = [int(x) for x in rounds[0].split(":")[1].split()]
        high_scores = [int(x) for x in rounds[1].split(":")[1].split()]

        for i in range(len(time)):
            possible_methods = 0
            for j in range(time[i]):
                if j * (time[i] - j) > high_scores[i]:
                    possible_methods += 1
            score = score * possible_methods if score > 0 else possible_methods

    return score


def part_two(value: str) -> int:
    score = 0

    filePath = path.join(getcwd(), "..", "data", value)

    with open(filePath, "r") as file:
        rounds = file.readlines()

        score_to_beat = int(rounds[1].split(":")[1].strip().replace(" ", ""))
        time_to_beat = int(rounds[0].split(":")[1].strip().replace(" ", ""))

        possible_scores = [0, 0]
        for j in range(time_to_beat):
            if j * (time_to_beat - j) > score_to_beat:
                possible_scores[0] = j
                break

        for j in range(time_to_beat, -1, -1):
            if j * (time_to_beat - j) > score_to_beat:
                possible_scores[1] = j
                break
        score = possible_scores[1] - possible_scores[0] + 1

    return score


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("test.txt"), 288)

    def test_part_1_solution(self):
        self.assertEqual(part_one("input.txt"), 633080)

    def test_part_two(self):
        self.assertEqual(part_two("test.txt"), 71503)

    def test_part_two_solution(self):
        self.assertEqual(part_two("input.txt"), 20048741)


if __name__ == "__main__":
    unittest.main()
