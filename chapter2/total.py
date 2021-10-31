# 학생 5명의 시험점수를 입력받아 합계와 평균을 출력

print('학생 그룹 점수의 합계와 평균')

score1 = int(input('1번 학생 점수 : '))
score2 = int(input('2번 학생 점수 : '))
score3 = int(input('3번 학생 점수 : '))
score4 = int(input('4번 학생 점수 : '))
score5 = int(input('5번 학생 점수 : '))

total = 0

total += score1
total += score2
total += score3
total += score4
total += score5

print(f'합계 {total}점')
print(f'평균 {total/5}점')
