def chinese_remainder(congruences):
   M = 1
   x = 0
   
   for _, n in congruences:
      M *= n

   for a_i, m_i in congruences:
      M_i = M // m_i
      M_i_inv = mod_inverse(M_i, m_i)
      x += a_i * M_i * M_i_inv

   return x % M


def extended_gcd(a, b):
   if b == 0:
      return a, 1, 0
   gcd, x1, y1 = extended_gcd(b, a % b)
   x = y1
   y = x1 - (a // b) * y1
   return gcd, x, y

def mod_inverse(a, m):
   gcd, x, _ = extended_gcd(a, m)
   if gcd != 1:
      raise ValueError(f"they need to be relative prime")
   return x % m

congruences = [(8, 9), (3,20)] 
solution = chinese_remainder(congruences)
print(f"The solution to the system of congruences is x = {solution}")
