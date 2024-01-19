def solution(n):
    answer = []
    num_list=list(map(int,str(n)))
    for i in range(len(num_list)):
        answer.append(num_list[len(num_list)-i-1])
    return answer

print(solution(12345))