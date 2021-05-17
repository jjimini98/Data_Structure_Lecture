# 피보나치 순열 - 재귀함수 

def solution(x):
   if x <= 1 : return x 
   else:
      return (solution(x-2) + solution(x-1))


print(solution(6))
print(solution(1))
print(solution(3))


