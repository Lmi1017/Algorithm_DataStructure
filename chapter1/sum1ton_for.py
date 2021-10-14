# 1부터 n까지 정수의 합 구하기2 (for)

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값 입력 : '))

sum = 0
for i in range(1, n+1):
    sum += i

print(f"1부터 {n}까지 정수의 합은 {sum}입니다.")
print(f"i값 : {i}")
