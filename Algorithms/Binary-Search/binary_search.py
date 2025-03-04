import math

def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index
        
        if mid_number < number_to_find:
            left_index = mid_index + 1

        if mid_number > number_to_find:
            right_index = mid_index - 1

    return -1

if __name__ == "__main__":
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67, 1]
    number_to_find = 45

    index = binary_search(numbers_list, number_to_find)
    print(index)

