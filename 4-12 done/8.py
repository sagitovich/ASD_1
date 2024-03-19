import random

array = []
for i in range(0, 10):
    array.append(random.randint(-100, 100))
print('Исходная последовательность:', *array)

positiv, negativ = [], []       # списки для полож. и отриц. эл-ов
for i in range(len(array)):     # раскидываем элементы по спискам
    if array[i] < 0:
        negativ.append(-array[i])
    else:
        positiv.append(array[i])
        

# Использование сортировки подсчета для сортировки элементов на основе значимых мест
def countingSort(array, place):
    size = len(array)       # фиксируем длину массива
    output = [0] * size     # создание списков на каждый элемент исходного списка
    count = [0] * 10    

    # считаем количество элементов
    for i in range(size):
        index = array[i] // place
        count[index % 10] += 1

    # считаем совокупное количество
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Разместите элементы в отсортированном порядке
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(size):
        array[i] = output[i]


# Основная функция 
def radixSort(array):
    # запоминаем максимальный элемент
    max_element = max(array)

    # Применяем сортировку подсчета для 
    # сортировки элементов на основе значения места
    place = 1
    while (max_element // place) > 0:
        countingSort(array, place)
        place *= 10

    return array

radixSort(negativ)
radixSort(positiv)

negativ.reverse()
for i in range(len(negativ)):
    negativ[i] = - negativ[i]

array = negativ + positiv

print('Отсортированная последовательнсть:', *(array))
