# 1부터 n까지 정수의 합 구하기 (while)

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값 입력: '))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f"1부터 {n}까지 정수의 합은 {sum}입니다.")
print(f"i값 : {i}")