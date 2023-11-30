import unittest


def main(value: int) -> int:
    return value * value


class Test(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(2), 4)


if __name__ == "__main__":
    unittest.main()
