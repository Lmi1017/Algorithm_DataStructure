def recur(n: int) -> int:
    if n > 0:
        recur(n-2)
        print(n)
        recur(n-1)


x = int(input('정숫값 입력 : '))

recur(x)
