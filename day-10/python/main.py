import unittest
from os import path, getcwd
import itertools
import math

import sys

sys.setrecursionlimit(100000)


def part_one(
    value: str, initial_dir: str, initial_x: int = 0, initial_y: int = 0
) -> int:
    score: int = 0
    filePath = path.join(getcwd(), "..", "data", value)

    with open(filePath, "r") as file:
        readings = [list(x) for x in file.read().split("\n")]

        start = {"x": 0, "y": 0}

        for i in range(len(readings)):
            for j in range(len(readings[i])):
                if readings[i][j] == "S":
                    start = {"x": j, "y": i}
                    break

        def get_reading(x: int, y: int):
            return readings[y][x]

        def get_next_coord(coordinates: [int, int], direction: str):
            reading = get_reading(coordinates[0], coordinates[1])
            if reading == "|":
                if direction == "d":
                    return [coordinates[0], coordinates[1] + 1, "d"]
                elif direction == "u":
                    return [coordinates[0], coordinates[1] - 1, "u"]
            elif reading == "-":
                if direction == "r":
                    return [coordinates[0] + 1, coordinates[1], "r"]
                elif direction == "l":
                    return [coordinates[0] - 1, coordinates[1], "l"]
            elif reading == "J":
                if direction == "d":
                    return [coordinates[0] - 1, coordinates[1], "l"]
                elif direction == "r":
                    return [coordinates[0], coordinates[1] - 1, "u"]

            elif reading == "F":
                if direction == "u":
                    return [coordinates[0] + 1, coordinates[1], "r"]
                elif direction == "l":
                    return [coordinates[0], coordinates[1] + 1, "d"]

            elif reading == "L":
                if direction == "d":
                    return [coordinates[0] + 1, coordinates[1], "r"]
                elif direction == "l":
                    return [coordinates[0], coordinates[1] - 1, "u"]
            elif reading == "7":
                if direction == "u":
                    return [coordinates[0] - 1, coordinates[1], "l"]
                elif direction == "r":
                    return [coordinates[0], coordinates[1] + 1, "d"]

        def get_scores(current_coords, score=1, direction="d"):
            next_coords = get_next_coord(current_coords, direction)
            if get_reading(next_coords[0], next_coords[1]) == "S":
                return score
            else:
                return get_scores(
                    [next_coords[0], next_coords[1]], score + 1, next_coords[2]
                )

        score = get_scores(
            [start["x"] + initial_x, start["y"] + initial_y], 1, initial_dir
        )

    return math.floor(score / 2) + 1


def part_two(
    value: str, initial_dir: str, initial_x: int = 0, initial_y: int = 0
) -> int:
    score: int = 0
    filePath = path.join(getcwd(), "..", "data", value)

    with open(filePath, "r") as file:
        readings = [list(x) for x in file.read().split("\n")]
        mapping = [[0 for y in range(len(readings[0]))] for x in range(len(readings))]

        start = {"x": 0, "y": 0}

        for i in range(len(readings)):
            for j in range(len(readings[i])):
                if readings[i][j] == "S":
                    start = {"x": j, "y": i}
                    break

        def get_reading(x: int, y: int):
            return readings[y][x]

        mapping[start["y"]][start["x"]] = 1

        def get_next_coord(coordinates: [int, int], direction: str):
            reading = get_reading(coordinates[0], coordinates[1])
            mapping[coordinates[1]][coordinates[0]] = 1
            if reading == "|":
                if direction == "d":
                    return [coordinates[0], coordinates[1] + 1, "d"]
                elif direction == "u":
                    return [coordinates[0], coordinates[1] - 1, "u"]
            elif reading == "-":
                if direction == "r":
                    return [coordinates[0] + 1, coordinates[1], "r"]
                elif direction == "l":
                    return [coordinates[0] - 1, coordinates[1], "l"]
            elif reading == "J":
                if direction == "d":
                    return [coordinates[0] - 1, coordinates[1], "l"]
                elif direction == "r":
                    return [coordinates[0], coordinates[1] - 1, "u"]

            elif reading == "F":
                if direction == "u":
                    return [coordinates[0] + 1, coordinates[1], "r"]
                elif direction == "l":
                    return [coordinates[0], coordinates[1] + 1, "d"]

            elif reading == "L":
                if direction == "d":
                    return [coordinates[0] + 1, coordinates[1], "r"]
                elif direction == "l":
                    return [coordinates[0], coordinates[1] - 1, "u"]
            elif reading == "7":
                if direction == "u":
                    return [coordinates[0] - 1, coordinates[1], "l"]
                elif direction == "r":
                    return [coordinates[0], coordinates[1] + 1, "d"]

        def get_scores(current_coords, score, direction):
            next_coords = get_next_coord(current_coords, direction)
            if get_reading(next_coords[0], next_coords[1]) == "S":
                return score
            else:
                return get_scores(
                    [next_coords[0], next_coords[1]], score + 1, next_coords[2]
                )

        get_scores([start["x"] + initial_x, start["y"] + initial_y], 1, initial_dir)

    inside_squares = []

    for i in range(len(mapping)):
        for j in range(len(mapping[0])):
            if mapping[i][j] == 1:
                continue
            else:
                # i = 2
                # j = 3
                squares_to_left = mapping[i][0:j]
                squares_to_right = mapping[i][j + 1 :]
                squares_above = [x[j] for x in mapping[0:i]]
                squares_below = [x[j] for x in mapping[i + 1 :]]

                if (
                    len(squares_to_left) == 0
                    and len(squares_to_right) == 0
                    and len(square_above) == 0
                    and len(squares_below) == 0
                ):
                    continue

                if (
                    sum(squares_to_left) % 2 == 1
                    and sum(squares_to_right) % 2 == 1
                    and sum(squares_above) % 2 == 1
                    and sum(squares_below) % 2 == 1
                ):
                    inside_squares.append(" ")

    return len(inside_squares)


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("test.txt", "d", 0, 1), 4)

    def test_part_one_two(self):
        self.assertEqual(part_one("test2.txt", "d", 0, 1), 8)

    def test_part_one_solution(self):
        self.assertEqual(part_one("input.txt", "d", 0, 1), 6717)

    def test_part_two(self):
        self.assertEqual(part_two("testPart2.txt", "d", 0, 1), 10)

    # def test_part_two_solution(self):
    #     self.assertEqual(part_two("input.txt"), 803)


if __name__ == "__main__":
    # unittest.main()
    print(part_two("testPart2.txt", "d", 0, 1))
