import random

a = []
for i in range(0, 10):
    a.append(random.randint(-100, 100))
print('Исходная последовательность:', *a)


def sort(array):
    n = len(array)
    step = n
    flag = True
    while step > 1 or flag:
        if step > 1:
            step = int(step / 1.247331)
        flag = False
        i = 0
        while i + step < n:
            if array[i] > array[i + step]:
                array[i], array[i + step] = array[i + step], array[i]
                flag = True
            i += step
    return array

a = sort(a)
print('Отсортированная последовательнсть:', *a)
