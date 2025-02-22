def binary_search(numbers_list, number_to_find, left_index, right_index):
    mid_index = (right_index + left_index) // 2
    count = 0

    if right_index < left_index:
        return 0

    if numbers_list[mid_index] == number_to_find:
        count += 1

        if mid_index != right_index:
            count += binary_search(numbers_list, number_to_find, mid_index + 1, right_index)

        if mid_index != left_index:
            count += binary_search(numbers_list, number_to_find, left_index, mid_index - 1)
    elif numbers_list[mid_index] > number_to_find:
        count += binary_search(numbers_list, number_to_find, left_index, mid_index - 1)
    elif numbers_list[mid_index] < number_to_find:
        count += binary_search(numbers_list, number_to_find, mid_index + 1, right_index)

    return count
    
if __name__ == "__main__":
    numbers = [1, 4, 5, 5, 5, 5, 7, 7, 9]
    number_to_find = 7

    occurance = binary_search(numbers, number_to_find, 0, len(numbers)-1)
    print(occurance)
