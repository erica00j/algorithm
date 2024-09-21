N = int(input())

array = []
for i in range(1,N+1):
    array.append(i)
used = [False for i in range(len(array))]

def backtrack_perm(arr):
    if len(arr)==N:
        print(' '.join(map(str, arr)))
        return

    for i in range(len(array)):
        if used[i]==False:
            used[i] = True
            backtrack_perm(arr+[array[i]])
            used[i] = False

backtrack_perm([])