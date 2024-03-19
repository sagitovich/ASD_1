import random
array = []
for i in range(0, 10):
    array.append(random.randint(-100, 100))
print('Исходная последовательность:', *array)

def merge(left,right,compare):
    result = [] 
    i,j = 0,0
    while (i < len(left) and j < len(right)):
        if compare(left[i],right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


def merge_sort(arr, compare = lambda x, y: x < y):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle], compare)
        right = merge_sort(arr[middle:], compare)
        return merge(left, right, compare)

print('Отсортированная последовательнсть:', *(merge_sort(array)))


