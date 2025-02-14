import heapq

def solution():
    N = int(input())

    times = []

    for i in range(N):
        times.append(list(map(int, input().split(" "))))

    times.sort()

    room = []

    maxLength = 0
    for i in range(N):
        if len(room) > 0:
            if room[0][0] <= times[i][0]:
                heapq.heappop(room)

        heapq.heappush(room, [times[i][1], times[i][0]])
        maxLength = max(maxLength, len(room))

    print(maxLength)

solution()