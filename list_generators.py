import random


def random_list(n: int) -> list:
    return [random.randint(-10, 10) for _ in range(n)]


def almost_reverse_list(n: int) -> list:
    res = [i - n / 2 for i in range(n, 0, -1)]
    res[n // 2], res[n // 2 + 1] = res[n // 2 + 1], res[n // 2]
    return res


def weird_list(n: int) -> list:
    res = list()
    for i in range(n):
        res.append(i % (n // 2))
    return res


def almost_ordered_list(n: int) -> list:
    ord_size = int(n * 0.95)
    return [i for i in range(ord_size)] + [
        random.randint(-10, 10) for _ in range(n - ord_size)
    ]


def nearby_positions_list(n: int) -> list:
    final_positions = [i for i in range(n)]
    res = []
    for pos in final_positions:
        deviation = random.randint(-10, 10)
        res.append(pos + deviation)
    return res


def insertion_sort(some_list: list) -> list:
    n = len(some_list)

    for i in range(n):
        j = i - 1
        key = some_list[i]
        while some_list[j] > key and j >= 0:
            some_list[j + 1] = some_list[j]
            j -= 1
        some_list[j + 1] = key

    return some_list
