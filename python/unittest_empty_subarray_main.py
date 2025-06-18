import unittest
from main import initialize_random_array, find_max_in_subarray, divide_array_into_subarrays

class TestArrayFunctions(unittest.TestCase):
    def test_divide_array_into_subarrays_zero_parts(self):
        original_input_array = [1, 2, 3]
        desired_number_of_subarrays = 0
        with self.assertRaises(ValueError):
            divide_array_into_subarrays(original_input_array, desired_number_of_subarrays)

    def test_find_max_in_empty_subarray(self):
        empty_input_subarray = []
        max_results_storage = [0] * 1
        with self.assertRaises(IndexError):
            find_max_in_subarray(empty_input_subarray, max_results_storage, 0)

if __name__ == '__main__':
    unittest.main()
