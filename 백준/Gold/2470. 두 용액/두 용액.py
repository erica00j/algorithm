import sys

N = int(sys.stdin.readline())
solution = list(map(int,sys.stdin.readline().split()))
solution.sort()

start = 0
end = N - 1
answer = abs(solution[start]+solution[end])
point = [solution[start],solution[end]]

while start < end:
    solution_sum = solution[start]+solution[end]
    if answer > abs(solution_sum):
        answer = abs(solution_sum)
        point = [solution[start],solution[end]]
        if answer == 0:
            break
    if solution_sum < 0:
        start += 1
    else:
        end -= 1

print(point[0],point[1])