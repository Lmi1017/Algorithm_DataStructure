# + 와 - 를 번갈아 출력하기 1

print('+와 -를 번갈아 출력')
n = int(input('몇 개를 출력하까요? '))

for i in range(n):
    if i % 2:
        print('-', end='')
    else:
        print('+', end='')

print()
