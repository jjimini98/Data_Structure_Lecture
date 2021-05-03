def solution(L, x):
   answer = []

   for l in range(len(L)):
     
      if x == L[l] : 
         
         answer.append(l) 
         continue

      if x not in L:
         return [-1]
   
   return answer


L = [64, 72, 83, 72, 54]  
x = 49

print(solution(L,x))