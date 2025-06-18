import unittest
from main import initialize_random_array, find_max_in_subarray, divide_array_into_subarrays

class TestArrayFunctions(unittest.TestCase):
    def test_initialize_random_array(self):
        expected_array_size = 10
        minimum_value_for_random_array = 0
        maximum_value_for_random_array = 100
        generated_random_array = initialize_random_array(expected_array_size, minimum_value_for_random_array, maximum_value_for_random_array)
        self.assertEqual(len(generated_random_array), expected_array_size)
        self.assertTrue(all(minimum_value_for_random_array <= element <= maximum_value_for_random_array for element in generated_random_array))

    def test_initialize_random_array_empty(self):
        empty_generated_array = initialize_random_array(0, 0, 10)
        self.assertEqual(empty_generated_array, [])

    def test_initialize_random_array_negative_values(self):
        generated_negative_value_array = initialize_random_array(10, -10, 0)
        self.assertTrue(all(-10 <= element <= 0 for element in generated_negative_value_array))

    def test_divide_array_into_subarrays(self):
        original_input_array = [1, 2, 3, 4, 5]
        desired_number_of_subarrays = 3
        divided_subarrays = divide_array_into_subarrays(original_input_array, desired_number_of_subarrays)
        total_elements_in_divided_subarrays = sum(len(subarray) for subarray in divided_subarrays)
        self.assertEqual(total_elements_in_divided_subarrays, len(original_input_array))
        self.assertEqual(len(divided_subarrays), desired_number_of_subarrays)

    def test_divide_array_into_subarrays_more_parts_than_elements(self):
        original_input_array = [1, 2]
        desired_number_of_subarrays = 5
        divided_subarrays = divide_array_into_subarrays(original_input_array, desired_number_of_subarrays)
        self.assertEqual(len(divided_subarrays), desired_number_of_subarrays)
        self.assertTrue(all(len(subarray) <= 1 for subarray in divided_subarrays))

    def test_divide_array_into_subarrays_zero_parts(self):
        original_input_array = [1, 2, 3]
        desired_number_of_subarrays = 0
        with self.assertRaises(ValueError):
            divide_array_into_subarrays(original_input_array, desired_number_of_subarrays)

    def test_find_max_in_subarray(self):
        input_subarray = [1, 3, 2, 5, 4]
        max_results_storage = [0] * 1  # Массив для хранения результата
        find_max_in_subarray(input_subarray, max_results_storage, 0)
        self.assertEqual(max_results_storage[0], max(input_subarray))

    def test_find_max_in_empty_subarray(self):
        empty_input_subarray = []
        max_results_storage = [0] * 1
        with self.assertRaises(IndexError):
            find_max_in_subarray(empty_input_subarray, max_results_storage, 0)

    def test_find_max_in_single_element_subarray(self):
        single_element_subarray = [42]
        max_results_storage = [0] * 1
        find_max_in_subarray(single_element_subarray, max_results_storage, 0)
        self.assertEqual(max_results_storage[0], 42)

    def test_find_max_in_negative_numbers(self):
        negative_numbers_subarray = [-1, -3, -2, -5, -4]
        max_results_storage = [0] * 1
        find_max_in_subarray(negative_numbers_subarray, max_results_storage, 0)
        self.assertEqual(max_results_storage[0], -1)

    def test_find_max_in_mixed_numbers(self):
        mixed_numbers_subarray = [-1, 3, -2, 5, -4]
        max_results_storage = [0] * 1
        find_max_in_subarray(mixed_numbers_subarray, max_results_storage, 0)
        self.assertEqual(max_results_storage[0], 5)

if __name__ == '__main__':
    unittest.main()
