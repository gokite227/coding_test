def solution(num):
    answer = 0
    while answer > 3:
        if num % 2 == 0 :
            num = num/2
            answer += 1
            print(answer)
        else :
            num = (num*3) + 1
            answer += 1
            print(answer)
    return answer