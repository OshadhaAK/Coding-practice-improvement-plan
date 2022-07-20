import unittest
import main


class TestMain(unittest.TestCase):

    def testFindMinimumMinutes(self):
        self.assertEqual(
            main.findMinimumMinuteDifference(["23:59", "00:00"]), 1)
        self.assertEqual(main.findMinimumMinuteDifference(
            ["00:00", "23:59", "00:00"]), 0)


if __name__ == "__main__":
    unittest.main()
