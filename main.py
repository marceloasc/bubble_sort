

def is_sorted(input_list: list[int]) -> bool:
    for index in range(1, len(input_list)):
        if input_list[index] < input_list[index-1]:
            return False
    return True

print(is_sorted(input_list=[1, 2, 3, 4, 5]))
