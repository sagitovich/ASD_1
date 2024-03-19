x = int(input('Введите верхнюю границу диапазона: '))
answ = []

for i in range(100):
    for j in range(100):
        for k in range(100):
            number = 3 ** i * 5 ** j * 7 ** k 

            if number <= x:
                answ.append(number)

cnt = 1
for a in sorted(answ):
    print(cnt, ') ', a, sep='')
    cnt += 1

