def recur(n: int) -> int:
    while n > 0:
        recur(n-1)
        print(n)
        n = n - 2


x = int(input('정숫값 입력 : '))

recur(x)
