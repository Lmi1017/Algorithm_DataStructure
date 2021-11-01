# 배열 원소의 최댓값을 구해서 출력하기(원솟값을 난수로 생성)

import random
from max import max_of

print('난수의 최댓값을 구함')
num = int(input('난수의 개수를 입력 : '))
lo = int(input('난수의 최솟값 입력 : '))
hi = int(input('난수의 최댓값 입력 : '))
x = [None]*num

for i in range(num):
    x[i] = random.randint(lo, hi)

print(f'{(x)}')
print(f'이 가운데 최댓값은 {max_of(x)}')
