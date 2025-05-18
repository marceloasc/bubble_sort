"""Bubble sort algorithm implementation."""

def bubble_sort(input_list: list[int]) -> list[int]:
    """
    Sorts a list of integers in ascending order using the Bubble Sort algorithm.

    The algorithm repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. The process is repeated until
    the list is sorted.

    Args:
        input_list (list[int]): The list of integers to be sorted.

    Returns:
        list[int]: The sorted list in ascending order.
    """
    iteration = 0
    for index1 in range(len(input_list)):
        iteration += 1
        for index2 in range(1, len(input_list)-index1):
            max_value = input_list[index2]
            if input_list[index2] < input_list[index2-1]:
                input_list[index2] = input_list[index2-1]
                input_list[index2-1] = max_value

        print(f"List after iteration {iteration}: {input_list}")

    return input_list


if __name__ == '__main__':
    input_list = "Declare list here, example: [5, 4, 3, 2, 1]."
    input_list_sorted = bubble_sort(input_list.copy())
    print(f"The list {input_list} sorted: {input_list_sorted}")
