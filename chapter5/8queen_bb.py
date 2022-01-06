pos = [0]*8
flag = [False] * 8


def put() -> None:
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()


def set(i: int) -> None:
    for j in range(8):
        if not flag[j]:
            pos[i] = j
            if i == 7:
                put()
            else:
                flag[j] = True
                set(i+1)
                flag[j] = False


set(0)
