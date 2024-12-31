def modular_exponentiation(base, exponent, mod):

   result = 1
   base = base % mod  

   while exponent > 0:
      
      if exponent % 2 == 1:
         result = (result * base) % mod

      
      exponent = exponent // 2
      base = (base * base) % mod

   return result

a = 23
b = 1024
n = 30
print(f"{a}^{b} mod {n} = {modular_exponentiation(a, b, n)}")
