# a부터 b까지 정수의 합 구하기(for문)

print('a부터 b까지 정수의 합 구하기')

print('[a, b  입력]')
a = int(input('a : '))
b = int(input('b : '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b+1):
    sum += i # 단일 대입문 (a와 b의 값을 교환)

print(f'{a}부터 {b}까지의 합은 {sum}')
