import math

def fermat_factorization(n):
   if n % 2 == 0:
      return n // 2, 2  
   
   a = math.ceil(math.sqrt(n))
   b2 = a * a - n  
   
   while not math.isqrt(b2) ** 2 == b2: 
      a += 1
      b2 = a * a - n 
   
   b = math.isqrt(b2)  
   return a - b, a + b


n = int(input("m = "))
factor1, factor2 = fermat_factorization(n)
print(f"the factore of  {n}  is {factor1} and {factor2}")
