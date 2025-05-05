# welkcom to rabin crypto sytem one of the most intersting crypto sytem
# spcialliy with no injective proprety 
# in the name of allah let't start ^_^

import random

# -----------------------1st step key genration 

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


def genreate_tow_random_prime_gcd_3(min_val,max_val):
   n1 = random.randint(min_val, max_val)
   n2 = random.randint(min_val, max_val)
   n1_mod_4 =  n1 % 4
   n2_mod_4 = n2 % 4
   while not is_prime(n1) or not is_prime(n2) or n1_mod_4 ==3 or n2_mod_4 == 3:
      n1 = random.randint(min_val, max_val)
      n2 = random.randint(min_val, max_val)
      n1_mod_4 =  n1 % 4
      n2_mod_4 = n2 % 4
   return n1,n2

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


# the priavte key is p,q 2 random prime number with GCD(p,q) = 3
p,q = genreate_tow_random_prime_gcd_3(65,200)
print(f"the priavte key (p = {p} , q = {q})")

p,q = 19,31

#  n is the finite feild Z/nZ and also the public key 
n = p * q 
print(f"the public key n = {n}")

message = input("please enter the message : ")
encoded_message = [ord(c) for c in message]
print("-"*100)
print(f"the encoded_message ---------> {encoded_message}")
print("-"*100)


# --------------------2nd step is enctption wich is very easy
crypted_encoded_message = []
for trunk in encoded_message :
   crypted_trunk = pow(trunk,2,n)
   crypted_encoded_message.append(crypted_trunk) 

print("crypted encoded message: \n-->  ",crypted_encoded_message)
crypted_message = "".join(chr (c) for c in crypted_encoded_message)
print(f"the crypted_message --> {crypted_message}")

# ------------------------3rd step decryption wich has a lot of caulc
# here we have 4 possible decrepted message
# m1 = p * m_q  * x + q * m_p * y 
# m2 = n + m1
# m3 = p * m_p * x - q * m_q * y 
# m4 = n - m3
decrepted_encoded_mesage = []
pow_p = int((1/4) * (p+1))
pow_q = int((1/4) * (q+1))

# to get the value of x and y we need to solve diophentine equation 
# the forme of the equation is :
#  c = a*x + b*y
# the equation has soultion if and onlay if GCD(a,b) is divisor of c <=> c / GCD(a,b) = intger
# the simplest way to solve tis equation is Bezout's Identity 
# we will use extend eclidan algorithem 

_,x,_ = exetende_ecldain(p,q)

if q > p :
   y = -((p * x ) // q)
else : 
   y = -((q * x)  // p)




print(f"x = {x} , y={y}")

for crypted_trunk in crypted_encoded_message : 
   m_q = pow(crypted_trunk,pow_q,q)
   m_p = pow(crypted_trunk,pow_p,p)

   print(f"m_p = {m_p} , p ={p} , x = {x}")
   print(f"m_q = {m_q} , q ={q} , y = {y}")

   m1 = ((p * m_q * x )+ (q * m_p * y)) % n
   m2 = (n - m1) % n
   m3 = ((p * m_q * x) -( q * m_p * y) ) % n
   m4 = (n - m3 ) % n
   
   condidant_letter = []
   condidant_letter.append(m1)
   condidant_letter.append(m2)
   condidant_letter.append(m3)
   condidant_letter.append(m4)
   decrepted_encoded_mesage.append(condidant_letter)


print("-"*100)
print(f"the decrepted encoded  message ------> {decrepted_encoded_mesage}")
print("-"*100)

