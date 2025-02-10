n = int(input())
current, count = 1, 1
if n == 0:
    print(0)
    exit()
while current < n:
    current *= 2
    count += 1
print(count)