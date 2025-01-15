import sys

N, M = map(int,sys.stdin.readline().split())
dot = list(map(int,sys.stdin.readline().split()))
dot.sort()

def dot_min(start_dot):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if start_dot > dot[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1

def dot_max(end_dot):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if end_dot >= dot[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return end

for i in range(M):
    count = 0
    start_dot, end_dot = map(int,sys.stdin.readline().split())
    print(dot_max(end_dot)-dot_min(start_dot)+1)