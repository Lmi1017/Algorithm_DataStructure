# 세 정수를 입력받아 최댓값 구하기
print('세 정수의 최댓값을 구합니다.')

a = int(input('integer a :'))
b = int(input('integer b :'))
c = int(input('integer c :'))

maximum = a
if b > maximum:
  maximum = b
if c > maximum:
  maximum = c

print(f"max value : {maximum}")