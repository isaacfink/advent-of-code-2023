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


def part_two(value: str) -> int:
    filePath = path.join(getcwd(), "..", "data", value)
    with open(filePath, "r") as file:
        return 0


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
    print(part_two("input.txt"))
