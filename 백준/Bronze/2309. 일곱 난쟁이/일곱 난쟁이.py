result = []
for i in range(9):
    height = int(input())
    result.append(height)
result.sort()
sum = sum(result)
answer = sum
found = False

while True:
    for i in range(8):
        for j in range(i+1, 9):
            answer -= result[i]
            answer -= result[j]
            if answer == 100:
                result.remove(result[j])
                result.remove(result[i])
                found = True
                break
            else:
                answer = sum
        if found:
            break  # 'while' 루프 탈출
    if found:
        break  # 'while' 루프 탈출

for x in result:
    print(x)