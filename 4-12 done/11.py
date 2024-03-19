import random

a = []
for i in range(0, 10):
    a.append(random.randint(-100, 100))
print('Исходная последовательность:', *a)


def sort(array):
    
    if len(array) <= 1:
        return array
    else:
        q = random.choice(array)
        l_nums = [n for n in array if n < q]

    e_nums = [q] * array.count(q)
    b_nums = [n for n in array if n > q]
    return sort(l_nums) + e_nums + sort(b_nums)

a = sort(a)
print('Отсортированная последовательнсть:', *a)

