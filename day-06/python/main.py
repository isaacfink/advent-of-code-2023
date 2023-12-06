import unittest
from os import path, getcwd


def part_one(value: str) -> int:
    score = 0

    filePath = path.join(getcwd(), "..", "data", value)

    with open(filePath, "r") as file:
        rounds = file.readlines()
        time = [int(x) for x in rounds[0].split(":")[1].split()]
        high_scores = [int(x) for x in rounds[1].split(":")[1].split()]
        # high_scores = int(rounds[1].strip().split(":")[1])
        print(time, high_scores)

        for i in range(len(time)):
            score_to_beat = high_scores[i]
            time_to_beat = time[i]
            possible_methods = 0

            for j in range(time_to_beat):
                achieved_score = j * (time_to_beat - j)
                if achieved_score > score_to_beat:
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
        possible_methods = 0

        lowest_possible = 0
        highest_possible = 0
        for j in range(time_to_beat):
            achieved_score = j * (time_to_beat - j)
            if achieved_score > score_to_beat:
                lowest_possible = j
                break

        for j in range(time_to_beat, -1, -1):
            achieved_score = j * (time_to_beat - j)
            if achieved_score > score_to_beat:
                highest_possible = j
                break
        score = highest_possible - lowest_possible + 1

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
