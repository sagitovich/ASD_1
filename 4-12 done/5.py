import random

a = []
for i in range(0, 10):
    a.append(random.randint(-100, 100))
print('Исходная последовательность:', *a)


def sort(array):
    for i in range(len(array)):
        j = i - 1
        temp = array[i]
        while array[j] > temp and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    return array


sort(a)
print('Отсортированная последовательнсть:', *a)

