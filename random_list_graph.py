import timeit
import random
import matplotlib.pyplot as plt


def random_list(n: int) -> list:
    return [random.randint(-10, 10) for _ in range(n)]


def insertion_sort(some_list: list) -> list:
    n = len(some_list)

    for i in range(n):
        j = i - 1
        key = some_list[i]
        while some_list[j] > key and j >= 0:
            some_list[j + 1] = some_list[j]
            j -= 1
        some_list[j + 1] = key
    print(some_list)
    return some_list


test_function = "insertion_sort(x)"

foo_timer = timeit.Timer(test_function, globals=globals())

plt_x = []
plt_y = []

for i in [100, 500, 1000, 2000, 4000, 6000, 8000, 10000]:
    x = random_list(i)
    print(x)
    plt_x.append(len(x))

    pt = foo_timer.timeit(number=1)
    plt_y.append(pt)


plt.plot(plt_x, plt_y)
plt.show()
