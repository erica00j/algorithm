N = int(input())
answer = 666
count = 0
while True:
    if '666' in str(answer):
        count += 1
    if count == N:
        break
    answer += 1
print(answer)