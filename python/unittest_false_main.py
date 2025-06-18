import unittest
from main import initialize_random_array, find_max_in_subarray, divide_array_into_subarrays

class TestArrayFunctions(unittest.TestCase):
    
    def test_initialize_random_array_with_strings(self):
        expected_array_size = 10
        minimum_value_for_random_array = 0
        maximum_value_for_random_array = 100
        with self.assertRaises(TypeError):
            initialize_random_array(expected_array_size, minimum_value_for_random_array, maximum_value_for_random_array, data_type=str)

    def test_find_max_in_subarray_with_strings(self):
        string_input_subarray = ['apple', 'banana', 'cherry']
        max_results_storage = [None]  # Используем None вместо 0 для хранения результата
        find_max_in_subarray(string_input_subarray, max_results_storage, 0)
        self.assertEqual(max_results_storage[0], 'cherry')

    def test_find_max_in_mixed_numbers_and_strings(self):
        mixed_input_subarray = [3, 'apple', 5, 'banana']
        max_results_storage = [None]  # Используем None вместо 0 для хранения результата
        with self.assertRaises(TypeError):
            find_max_in_subarray(mixed_input_subarray, max_results_storage, 0)

    def test_divide_array_into_subarrays_with_strings(self):
        original_string_input_array = ['one', 'two', 'three']
        desired_number_of_string_subarrays = 2
        divided_string_subarrays = divide_array_into_subarrays(original_string_input_array, desired_number_of_string_subarrays)
        total_elements_in_divided_string_subarrays = sum(len(subarray) for subarray in divided_string_subarrays)
        self.assertEqual(total_elements_in_divided_string_subarrays, len(original_string_input_array))
        self.assertEqual(len(divided_string_subarrays), desired_number_of_string_subarrays)

if __name__ == '__main__':
    unittest.main()
