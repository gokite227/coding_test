#
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)) :
        ans = []
        for j in range(len(arr1[i])):
            ans.append(arr1[i][j]+arr2[i][j])
        answer.append(ans)
    return answer

###
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

###
def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A