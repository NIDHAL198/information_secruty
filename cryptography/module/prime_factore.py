# -------------- breack the RSA -----------------

def prime_factors(n):
   factors = list()
   while n % 2 == 0:
      factors.append(2)
      n //= 2
   f = 3
   while f * f <= n:
      while n % f == 0:
         factors.append(f)
         n //= f
      f += 2
   if n > 1:
      factors.append(n)
   return factors

x = int(input("enter the value"))
prime_fact = prime_factors(x)
print(prime_fact)