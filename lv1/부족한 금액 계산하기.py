def solution(price, money, count):
    a=0
    for i in range(1,count+1,1):
        a+=price*i
    if money>=a:
        return 0
    else:
        return abs(money-a)