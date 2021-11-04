# 각 배열 원소의 최댓값을 구패서 출력하기 (튜플, 문자열, 문자열 리스트)
from max import max_of

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

# 가장 큰 수 출력
print(f'{t}의 최댓값은 {max_of(t)}')

# 문자열 중 가장 큰 문자 출력
print(f'{s}의 최댓값은 {max_of(s)}')

# 사전 순으로 가장 큰 문자열 출력
print(f'{a}의 최댓값은 {max_of(a)}')