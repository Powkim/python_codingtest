import math
def solution(n, k):
    totalService=math.floor((n/10))
    answer = (n*12000)+(k*2000)-(totalService*2000)
    return answer