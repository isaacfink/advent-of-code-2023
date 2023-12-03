import unittest
from os import path, getcwd
import re


def part_one(value: str) -> int:
    score = 0

    maxCounts = {
        "blue": 14,
        "green": 13,
        "red": 12,
    }
    filePath = path.join(getcwd(), "data", value)
    with open(filePath, "r") as file:
        data = file.read().splitlines()
        for game in data:
            splitGame = game.split(":")
            id = splitGame[0].strip().split(" ")[1]
            rounds = splitGame[1].split(";")
            gameIsPossible = True
            for round in rounds:
                colors = round.strip().split(",")
                for color in colors:
                    colorSplit = color.strip().split(" ")
                    colorCount = int(colorSplit[0].strip())
                    colorName = colorSplit[1].strip()
                    if colorCount > maxCounts[colorName]:
                        gameIsPossible = False
                        break

            if gameIsPossible:
                score += int(id)
    return score


def part_two(value: str) -> int:
    score = 0
    filePath = path.join(getcwd(), "data", value)
    with open(filePath, "r") as file:
        data = file.read().splitlines()
        for game in data:
            maxCounts = {
                "blue": 0,
                "green": 0,
                "red": 0,
            }
            splitGame = game.split(":")
            id = splitGame[0].strip().split(" ")[1]
            rounds = splitGame[1].split(";")
            gameIsPossible = True
            for round in rounds:
                colors = round.strip().split(",")
                for color in colors:
                    colorSplit = color.strip().split(" ")
                    colorCount = int(colorSplit[0].strip())
                    colorName = colorSplit[1].strip()
                    if colorCount > maxCounts[colorName]:
                        maxCounts[colorName] = colorCount

            if gameIsPossible:
                score += maxCounts["blue"] * maxCounts["green"] * maxCounts["red"]
    return score


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("test.txt"), 8)

    def test_part_two(self):
        self.assertEqual(part_two("test.txt"), 2286)


if __name__ == "__main__":
    unittest.main()
