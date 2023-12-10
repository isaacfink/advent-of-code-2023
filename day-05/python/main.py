import unittest
from os import path, getcwd

items = [
    "seed",
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location",
]


def part_one(value: str) -> int:
    score = None

    filePath = path.join(getcwd(), "..", "data", value)
    results = []

    with open(filePath, "r") as file:
        sections = file.read().split("\n\n")

        for index, section in enumerate(sections[1::]):
            lines = section.split("\n")[1::]
            res = {
                "source_name": items[index],
                "dest_name": items[index + 1],
                "source": [],
                "dest": [],
            }
            for line in lines:
                [dest_start, source_start, range_num] = [
                    int(x.strip()) for x in line.split()
                ]
                res["source"].append((source_start, source_start + range_num))
                res["dest"].append((dest_start, dest_start + range_num))

            results.append(res)

        seeds = [int(x) for x in sections[0].split(":")[1].split()]

        for seed in seeds:
            id = seed
            for result in results:
                for index, nums_range in enumerate(result["source"]):
                    if nums_range[0] <= id <= nums_range[1]:
                        id = result["dest"][index][0] + (id - nums_range[0])
                        break
            score = min(score, id) if score else id

    return score if score else 0


def calculate_ranges(t1: list[int], t2: list[int]):
    # Extracting the start and end points of both tuples
    start1, end1 = t1
    start2, end2 = t2

    # Finding the intersection
    intersect_start = max(start1, start2)
    intersect_end = min(end1, end2)

    if intersect_start <= intersect_end:
        # There is an intersection
        intersection = (max(start1, start2), max(end1, end2))

        # Finding the remaining ranges
        remaining_ranges = []
        if start1 < intersect_start:
            remaining_ranges.append((start1, intersect_start - 1))
        if end1 > intersect_end:
            remaining_ranges.append((intersect_end + 1, end1))
    else:
        # No intersection
        intersection = None
        remaining_ranges = [t1]  # Original ranges are the remaining ranges

    return intersection, remaining_ranges


def part_two(value: str) -> int:
    score = None

    filePath = path.join(getcwd(), "..", "data", value)
    results = []

    with open(filePath, "r") as file:
        sections = file.read().split("\n\n")

        for index, section in enumerate(sections[1::]):
            lines = section.split("\n")[1::]
            res = {
                "source_name": items[index],
                "dest_name": items[index + 1],
                "source": [],
                "dest": [],
            }
            for line in lines:
                [dest_start, source_start, range_num] = [
                    int(x.strip()) for x in line.split()
                ]
                res["source"].append((source_start, source_start + range_num))
                res["dest"].append((dest_start, dest_start + range_num))

            results.append(res)

        seeds = [int(x) for x in sections[0].split(":")[1].split()]

        seed_ranges = [
            [seeds[x], seeds[x] + seeds[x + 1]] for x in range(0, len(seeds), 2)
        ]

        current_ranges = seed_ranges

        for r in current_ranges:
            for result in results:
                intersecting = []
                additional_ranges = []

                intersecting, ranges = calculate_ranges(r, result["dest"][0])

    return score if score else 0


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("test.txt"), 35)

    # def test_part_1_solution(self):
    #     self.assertEqual(part_one("input.txt"), 28538)

    def test_part_two(self):
        self.assertEqual(part_two("test.txt"), 46)

    # def test_part_two_solution(self):
    #     self.assertEqual(part_two("input.txt"), 9425061)


if __name__ == "__main__":
    # unittest.main()
    print(part_two("test.txt"))
