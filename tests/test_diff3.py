import unittest
import diff3lib

class TestDiffFunction(unittest.TestCase):

    def test_00(self):
        self.assertEqual(
            diff3lib.diff(
                ['a', 'b', 'c', 'f', 'g', 'h', 'i', 'j'],
                ['a', 'B', 'c', 'd', 'e', 'f', 'j']),
            [['c', 2, 2, 2, 2], ['a', 4, 3, 4, 5], ['d', 5, 7, 7, 6]])

    def test_01(self):
        self.assertEqual(
            diff3lib.diff(
                ['a', 'b', 'c'],
                ['A', 'a', 'b', 'c']),
            [['a', 1, 0, 1, 1]])

    def test_02(self):
        self.assertEqual(
            diff3lib.diff(
                ['a', 'b', 'c'],
                ['a', 'b', 'c', 'D']),
            [['a', 4, 3, 4, 4]])

    def test_03(self):
        self.assertEqual(
            diff3lib.diff(
                ['A', 'b', 'c'],
                ['b', 'c']),
            [['d', 1, 1, 1, 0]])

    def test_04(self):
        self.assertEqual(
            diff3lib.diff(
                ['a', 'B', 'c'],
                ['a', 'c']),
            [['d', 2, 2, 2, 1]])

    def test_05(self):
        self.assertEqual(
            diff3lib.diff(
                ['a', 'b', 'C'],
                ['a', 'b']),
            [['d', 3, 3, 3, 2]])

class TestDiff3Function(unittest.TestCase):

    def test_10(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'B', 'C', 'D', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f']),
            [['0', 2,4, 2,4, 2,4]])

    def test_11(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'B', 'C', 'D', 'E', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f']),
            [['2', 2,5, 2,5, 2,5]])

    def test_12(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'C', 'D', 'E', 'f']),
            [['1', 3,5, 3,5, 3,5]])

    def test_13(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'w', 'x', 'y', 'z', 'f'],
                ['a', 'B', 'C', 'D', 'E', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f']),
            [['A', 2,5, 2,5, 2,5]])

    def test_14(self):
        self.assertEqual(
            diff3lib.diff3(
                ['c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f']),
            [['0', 1,0, 1,2, 1,2]])

    def test_15(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'b', 'c', 'd'],
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f']),
            [['0', 5,4, 5,6, 5,6]])

    def test_16(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a','c', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f']),
            [['0', 2,1, 2,2, 2,2], ['0', 3,2, 4,4, 4,4]])

    def test_17(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['c', 'd', 'e', 'f']),
            [['1', 1,2, 1,0, 1,2]])

    def test_18(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd']),
            [['1', 5,6, 5,4, 5,6]])

    def test_19(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a','c', 'e', 'f']),
            [['1', 2,2, 2,1, 2,2], ['1', 4,4, 3,2, 4,4]])

    def test_1a(self):
        self.assertEqual(
            diff3lib.diff3(
                ['A', 'A', 'a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f']),
            [['0', 1,2, 1,0, 1,0]])

    def test_1b(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'b', 'c', 'd', 'e', 'f', 'G', 'G'],
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f']),
            [['0', 7,8, 7,6, 7,6]])

    def test_1c(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'B', 'B', 'b', 'c', 'D', 'D', 'D', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f']),
            [['0', 2,3, 2,1, 2,1], ['0', 6,8, 4,3, 4,3]])

    def test_1d(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['A', 'A', 'a', 'b', 'c', 'd', 'e', 'f']),
            [['1', 1,0, 1,2, 1,0]])

    def test_1e(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f', 'G', 'G']),
            [['1', 7,6, 7,8, 7,6]])

    def test_1f(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'B', 'B', 'b', 'c', 'D', 'D', 'D', 'd', 'e', 'f']),
            [['1', 2,1, 2,3, 2,1], ['1', 4,3, 6,8, 4,3]])

    def test_1g(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f']),
            [['2', 1,2, 1,2, 1,0]])

    def test_1h(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd'],
                ['a', 'b', 'c', 'd', 'e', 'f']),
            [['2', 5,6, 5,6, 5,4]])

    def test_1i(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'c', 'e', 'f'],
                ['a', 'b', 'c', 'd', 'e', 'f']),
            [['2', 2,2, 2,2, 2,1], ['2', 4,4, 4,4, 3,2]])

    def test_1j(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['c', 'd', 'e', 'f'],
                ['a', 'B', 'c', 'd', 'e', 'f']),
            [['A', 1,2, 1,2, 1,0]])

    def test_1k(self):
        self.assertEqual(
            diff3lib.diff3(
                ['a', 'b', 'c', 'd', 'e', 'f'],
                ['a', 'b', 'c', 'd'],
                ['a', 'b', 'c', 'd', 'e', 'F']),
            [['A', 5,6, 5,6, 5,4]])

    def test_1l(self):
        self.assertEqual(
            diff3lib.diff3(
                ['A', 'A', 'b', 'c', 'f', 'g', 'h', 'i', 'j', 'K', 'l',
                 'm', 'n', 'O', 'p', 'Q', 'R', 's'],
                ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'],
                ['a', 'b', 'c', 'd', 'f', 'j', 'K', 'l', 'M', 'n', 'o',
                 'p', '1', '2', 's', 't', 'u']),
            [
                ['0',  1, 2,  1, 1,  1, 1],
                ['A',  5, 4,  4, 4,  4, 5],
                ['1',  6, 8,  6, 5,  7, 9],
                ['2', 10,10,  7, 7, 11,11],
                ['1', 12,12,  9, 9, 13,13],
                ['0', 14,14, 11,11, 15,15],
                ['A', 16,17, 13,14, 17,18],
                ['1', 19,18, 16,17, 20,19],
            ])

if __name__ == '__main__':
    unittest.main()

