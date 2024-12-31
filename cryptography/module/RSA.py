import random

def is_prime(number) : 
   if number <= 1 :
      return False
   if number <= 3 :
      return True
   if number % 2 == 0 :
      return False
   
   for num in range(3,int(number**0.5) +1 ,2) :
      if number % num == 0:
         return False

   return True

def genreate_prime_number(min_val,max_val):
   prime = random.randint(min_val, max_val)
   while not is_prime(prime):
      prime = random.randint(min_val, max_val)
   return prime

def ecludiane(a,b) : 

   num1 = a if a > b else b 
   num2  = a if a < b else b 

   if num2 == 0 :
      return num1
   
   while num2 !=0 :
      r = num1 % num2 
      num1 = num2 
      num2 = r
   return num1



def exetende_ecldain (e , PHI) :

   a = PHI if PHI > e else e
   b = PHI if PHI < e else e

   if b == 0 : 
      return a , 1 , 0

   pgcd = 1
   t1 = 0
   t2 = 1
   qutione = t  = 0
   while (b !=0 ) :
      qutione = a//b
      t = t1 - t2 * qutione
      reminder  = a%b
      a = b 
      b = reminder
      t1 = t2 
      t2 = t 
   pgcd = a
   return pgcd , t1 , t2

p,q = genreate_prime_number(1000,5000) , genreate_prime_number(1000,5000)
while p == q :
   q= genreate_prime_number(1000,5000)

n = p * q

PHI = 0

if  is_prime(n) :
   PHI  = n-1
else :
   PHI = (p-1) * (q-1)

e = random.randint(3,PHI -1) 
while ecludiane(e ,PHI) != 1  :
   e = random.randint(3,PHI - 1) 

_,d,_ = exetende_ecldain(e,PHI)
if d < 0 :
   d += PHI


print("p = ",p)
print("q = ",q)
print("n = ",n)
print("PHI = ",PHI)
print("public key e = ",e)
print("priavte key d = ",d)

message = input("please enter your messge ")

encoded_message = [ord(c) for c in message]
cipher_message = [pow(c,e,n) for c in encoded_message]
print("cipher message",cipher_message)

encoded_message = [pow(c,d,n) for c in cipher_message]
message = "".join(chr (c) for c in encoded_message)

print("the decrepted message",message)