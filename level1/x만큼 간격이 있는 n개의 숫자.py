def solution(x, n):
    answer = [x]
    plus = x
    for i in range(n-1):
        answer.append(plus+x)
        plus+=x
    return answer