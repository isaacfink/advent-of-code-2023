import unittest
from os import path, getcwd
import re
import itertools

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
regex = r"[^a-z0-9\.]"


def getNumbersInRow(row: list[str]):
    index = 0
    isPart: bool = False
    parts: list[list[int]] = []

    while index < len(row):
        char = row[index]
        if char in digits and not isPart:
            parts.append([index, index])
            isPart = True
        elif char in digits and isPart:
            parts[len(parts) - 1][1] = index
        else:
            isPart = False
        index += 1

    return parts


def part_one(value: str) -> int:
    score = 0

    filePath = path.join(getcwd(), "..", "data", value)
    with open(filePath, "r") as file:
        readings = [list(line.strip()) for line in file]

        def lowerEnd(index: int):
            return max(0, index)

        def higherEndRows(index: int):
            return min(len(readings[0]) - 1, index)

        def higherEndCols(index: int):
            return min(len(readings) - 1, index)

        def isSymbol(str: str):
            return re.search(regex, str) is not None

        for i in range(len(readings)):
            reading = readings[i]

            parts = getNumbersInRow([x for x in reading])
            for part in parts:
                start = lowerEnd(part[0] - 1)
                end = higherEndRows(part[1] + 1) + 1

                toScan = (
                    readings[lowerEnd(i - 1)][start:end]
                    + readings[i][start:end]
                    + readings[higherEndCols(i + 1)][start:end]
                )

                if isSymbol("".join(toScan)):
                    score += int("".join(reading[part[0] : part[1] + 1]))

    return score


def part_two(value: str) -> int:
    score = 0
    filePath = path.join(getcwd(), "..", "data", value)
    with open(filePath, "r") as file:
        readings = [list(line.strip()) for line in file]

        numbers = [getNumbersInRow(x) for x in readings]

        def getInRangeNumbersRows(index: int, row: list[list[int]]):
            return list(filter(lambda x: any(abs(num - index) >= 1 for num in x), row))

        for fileIndex in range(len(readings)):
            reading = readings[fileIndex]

            for i in range(len(reading)):
                char = reading[i]

                if char == "*":
                    rowIndex = [fileIndex]
                    if fileIndex > 0:
                        rowIndex.append(fileIndex - 1)
                    if fileIndex < len(readings) - 1:
                        rowIndex.append(fileIndex + 1)

                    rowsCombined = [numbers[x] for x in rowIndex]
                    flattened_list = list(itertools.chain(*rowsCombined))

                    numbersInRange = getInRangeNumbersRows(i, flattened_list)

                    if len(numbersInRange) == 2:
                        score += numbersInRange[0] * numbersInRange[1]

                    print(numbersInRange)

    return score


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("test.txt"), 4361)

    def test_part_1_solution(self):
        self.assertEqual(part_one("input.txt"), 553825)

    def test_part_two(self):
        self.assertEqual(part_two("test.txt"), 467835)


if __name__ == "__main__":
    unittest.main()
    # print(part_two("test.txt"))
