import unittest
from sorting_02.insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_insertion_sort_book_example(self):
        input_a = [5, 2, 4, 6, 1, 3]
        result_a = [1, 2, 3, 4, 5, 6]
        self.assertNotEqual(input_a, result_a)
        insertion_sort(input_a)
        self.assertEqual(input_a, result_a)


if __name__ == "__main__":
    unittest.main()
