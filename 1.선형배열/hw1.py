def solution(L, x):
    for t in L:
        if x < t:
            L.insert(L.index(t), x)
            break
        if x > max(L):
            L.insert(L.index(max(L))+1,x)


    return L

lis = [20, 37, 58, 72, 91]

print(solution(lis, 102))

