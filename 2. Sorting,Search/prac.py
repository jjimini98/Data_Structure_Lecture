# L = [2, 5, 7, 9, 11]
# x = 4
# print(L[4])
# mid_index = int(len(L)/2)

# for x in L[mid_index+1:]:
#    print(x)


def solution(L, x):
   mid =len(L)//2
   
   if x not in L: return -1 

   for t in range(len(L)):

      if x > L[mid] :
         if L[t] == x : return t


      elif x < L[mid]  :    
         if L[t] == x :  return t
         
      elif x == L[mid] : return mid 

      elif 


L = [2, 5, 7, 9, 11]
x = 9

print(solution(L,x))