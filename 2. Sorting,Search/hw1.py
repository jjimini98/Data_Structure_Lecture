# 이진탐색

# 시간초과..;; 
# def solution(L,x):
#     for l in L:
#         if l<x : continue
#         if x not in L: return -1
#         if x == l: return L.index(l)


# 효율성 테스트 실패  
# def solution(L, x):
#    mid_index = int(len(L)/2)
#    mid = L[mid_index]

#    if x not in L: return -1 

#    if x > mid :
#       for l in L[mid_index+1:]:
#         if l == x : return L.index(l)
   
#    elif x < mid  :    
#       for l in L[0:mid_index]:
#          if l == x : return L.index(l)

#    elif x == mid : return mid_index


# L = [2, 5, 7, 9, 11]
# x = 22

# print(solution(L,x))

def solution(L, x):
   mid =len(L)//2
   
   if x not in L: return -1 

   if x > L[mid] :
      if x in L[mid+1:]: return L.index(x)

   elif x < L[mid]  :    
      if x in L[0:mid]: return L.index(x)

   elif x == L[mid] : return L.index(x)


L = [2, 5, 7, 9, 11]
x = 9

print(solution(L,x))