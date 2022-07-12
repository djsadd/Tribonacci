# put your python code here
N = int(input())


def get_balakirev(n):
    start = 1
    step = 1
    middle = 1
    for j in range(0, n):
        if j < 3:
            yield 1
        else:
            z = start + step + middle
            yield z
            step = middle
            middle = start
            start = z


a = get_balakirev(N)

for j in a:
    print(j, end=' ')


