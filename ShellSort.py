import unittest

class ShellSort:
    @staticmethod
    def sort(arr):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2


class TestShellSort(unittest.TestCase):
    def test_shell_sort_case1(self):
        arr1 = [12, 34, 54, 2, 3]
        ShellSort.sort(arr1)
        self.assertEqual(arr1, [2, 3, 12, 34, 54])

    def test_shell_sort_case2(self):
        arr2 = [64, 25, 12, 22, 11]
        ShellSort.sort(arr2)
        self.assertEqual(arr2, [11, 12, 22, 25, 64])

if __name__ == "__main__":
    unittest.main()
