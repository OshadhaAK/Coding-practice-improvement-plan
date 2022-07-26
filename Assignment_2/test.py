import unittest
import main


class TestMain(unittest.TestCase):

    def testLargestSum(self):
        self.assertEqual(
            main.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(main.maxSubArray(
            [1]), 1)
        self.assertEqual(main.maxSubArray(
            [5, 4, -1, 7, 8]), 23)


if __name__ == "__main__":
    unittest.main()
