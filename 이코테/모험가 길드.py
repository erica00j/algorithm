N = 5
level = list(map(int,input().split()))
level.sort()

result=0
count=0

for i in level:
    count+=1
    if count>=i:
        result+=1
        count=0
print(result)

