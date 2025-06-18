import random
import threading

mutex = threading.Lock()

def initialize_random_array(array_size, min_value, max_value):
    try:
        return [random.randint(min_value, max_value) for _ in range(array_size)]
    except Exception as e:
        print(f"Error initializing random array: {e}")
        return []

def find_max_in_subarray(sub_array, max_results, subarray_index):
    try:
        max_element_in_subarray = max(sub_array)
        with mutex:
            max_results[subarray_index] = max_element_in_subarray
    except Exception as e:
        print(f"Error finding max in subarray {subarray_index}: {e}")

def divide_array_into_subarrays(original_array, number_of_subarrays):
    try:
        subarray_size = len(original_array) // number_of_subarrays
        remainder = len(original_array) % number_of_subarrays

        subarrays = []
        start_index = 0

        for subarray_index in range(number_of_subarrays):
            current_subarray_size = subarray_size + (1 if subarray_index < remainder else 0)
            sub_array = original_array[start_index:start_index + current_subarray_size]
            subarrays.append(sub_array)
            start_index += current_subarray_size

        return subarrays
    except Exception as e:
        print(f"Error dividing array into subarrays: {e}")
        return []

def main():
    try:
        random_array_size = random.randint(100, 200)
        min_random_value = 0
        max_random_value = 1000

        original_array = initialize_random_array(random_array_size, min_random_value, max_random_value)

        number_of_subarrays = random.randint(1, 10)
        print(f"Number of subarrays: {number_of_subarrays}")

        subarrays = divide_array_into_subarrays(original_array, number_of_subarrays)

        threads = []
        max_elements_from_subarrays = [0] * number_of_subarrays

        for subarray_index, sub_array in enumerate(subarrays):
            thread = threading.Thread(target=find_max_in_subarray, args=(sub_array, max_elements_from_subarrays, subarray_index))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        overall_maximum_value = max(max_elements_from_subarrays)

        print("Original Array:", original_array)
        print("Max elements from each subarray:", max_elements_from_subarrays)
        print("Overall maximum value:", overall_maximum_value)

    except Exception as e:
        print(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
