T = int(input())
for i in range(T):
    N = int(input())
    set_N = set(list(map(int,input().split())))
    M = int(input())
    list_M = list(map(int,input().split()))

    for j in list_M:
        if j in set_N:
            print(1)
        else:
            print(0)