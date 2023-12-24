def insertion_sort(some_list: list) -> list:
    shifts = 0  # число перестановок
    comparisons = 0
    n = len(some_list)

    for i in range(n):
        j = i - 1
        key = some_list[i]
        while some_list[j] > key and j >= 0:
            comparisons += 1
            some_list[j + 1] = some_list[j]
            shifts += 1
            j -= 1
        some_list[j + 1] = key
        shifts += 1

        print("i =", i, "array:", some_list)

    # comparisons = int((n) * n / 2)  # число сравнений (формула суммы ряда)

    print("Число перестановок:", shifts)
    print("Число сравнений:", comparisons)

    return some_list


test_list1 = [7, 3, 9, 4, 2, 5, 6, 1, 8]
test_list2 = [3, 5, 2, 9, 8, 1, 6, 4, 7]

print("original array:", test_list1)
print("result:", insertion_sort(test_list1), end="\n\n")

print("original array:", test_list2)
print("result:", insertion_sort(test_list2), end="\n\n")
