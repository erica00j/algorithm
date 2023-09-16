def solution(numbers):
    int_n=[1,2,3,4,5,6,7,8,9,0]
    for i in numbers:
        if i in int_n:
            int_n.remove(i)
    return sum(int_n)

# 0~9까지의 합 - sum(numbers)