# *를 n개 출력하되 w개마다 줄바꿈하기 2

print('*를 출력')
n = int(input('몇 개를 출력할까요?: '))
w = int(input('몇 마다 줄바꿈할까요?: '))

for i in range(n//w):
    print('*'*w)


rest = n % w
if rest:
    print('*'*rest)
