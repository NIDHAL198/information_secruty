import random

def miller_rabin(n, k=5):
   if n <= 1:
      return False
   if n <= 3:
      return True
   if n % 2 == 0:
      return False


   s, d = 0, n - 1
   while d % 2 == 0:
      s += 1
      d //= 2


   for _ in range(k):
      a = random.randint(2, n - 2) 
      x = pow(a, d, n)  
      if x == 1 or x == n - 1:
         continue  
      
      for _ in range(s - 1):
         x = pow(x, 2, n)
         if x == n - 1:
               break
      else:
         return False 
   
   return True 

n = int(input("n = "))
is_prime = miller_rabin(n)
print(f"the number {n} {"is prime number" if is_prime else "is compose number"}")
