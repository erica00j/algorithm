def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        result = 0
        for j in range(len(photo[i])):
            for k in range(len(name)):
                if photo[i][j] == name[k]:
                    result += yearning[k]   
        answer.append(result)
    return answer