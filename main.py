

def is_sorted(input_list: list[int]) -> bool:
    for index in range(1, len(input_list)):
        if input_list[index] < input_list[index-1]:
            return False
    return True

def bubble_sort(input_list: list[int]) -> list[int]:
    iteration = 0
    while not is_sorted(input_list):
        iteration += 1
        for index in range(1, len(input_list)):
            max_value = input_list[index]
            if input_list[index] < input_list[index-1]:
                input_list[index] = input_list[index - 1]
                input_list[index - 1] = max_value

        print(f"List after iteration {iteration}: {input_list}")

    return input_list


if __name__ == '__main__':
    input_list = [5, 4, 3, 2, 1]
    input_list_sorted = bubble_sort(input_list.copy())
    print(f"The list {input_list} sorted: {input_list_sorted}")
