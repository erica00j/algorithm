def solution(n):
    answer = 0
    num_list = list(map(int, str(n)))
    for i in num_list :
        answer+=i

    return answer

print(solution(987))