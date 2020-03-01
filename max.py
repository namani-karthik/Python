def solution(A):
    if(A==[]):
        return 'PAssed an empty list'
    max_value = max(A)
    i=max_value-1
    while(i>1):
        if(i in A):
            i-=1
        else:
            return i
    if(max_value <0):
        return 1
    return max_value + 1
        

print(solution([1,2,3]))
