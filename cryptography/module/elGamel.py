# the author -------> boulgamh lahcen nidhal (neither chatgpt nor deeepseek ^_*)

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

# --------------------------------first step key genration 

def genreate_random_prime(min_val,max_val):
   prime = random.randint(min_val, max_val)
   while not is_prime(prime):
      prime = random.randint(min_val, max_val)
   return prime

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

# the bothe side agree in the valuue of finite_feild
finite_feild = genreate_random_prime(320,500)


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


print(f"the finite feild ---> {finite_feild}")

# i will optimise the code later by loop onlay in the  coprime number of the finite feild
def primitive_root_generate(f_f):
   if f_f == 1:  # Special case
      return 0
   
   if f_f == 2:  # For modulo 2, 1 is the only primitive root
      return 1
   
   for candidate in range(2, f_f):
      list_generated_elements = []
      is_primitive_root = True
      
      for exp in range(1, f_f):
         el = pow(candidate, exp, f_f)
         if el in list_generated_elements:
               is_primitive_root = False
               break
         list_generated_elements.append(el)
      
      if is_primitive_root and len(list_generated_elements) == f_f - 1:
         return candidate
   
   return None  

# the bothe side agree in the valuue of finite_feild
premtive_root = primitive_root_generate(finite_feild)

if premtive_root is not None:
   print(f"The primitive root of Z/{finite_feild}Z is {premtive_root}")
else:
   print("No primitive root found")


def eclude(num1, num2) :
   a = num1 if num1 > num2 else num2
   b = num1 if num1 < num2 else num2
   pgcd = 1
   if b == 0 :
      return a 
   else : 
      while b != 0 :
         q = a // b
         r = a % b 
         a =b 
         b = r
         pgcd = a
      return pgcd


def gerate_private_key(f_f) :
   p_k = random.randint(2,f_f-1)
   while eclude(p_k,f_f) != 1 or not is_prime(p_k) :
      p_k = random.randint(2,f_f-1)
   return p_k

# the  genration of private and the public key is in the side of the recever

private_key = gerate_private_key(finite_feild)



print(f"the private_key  ----> {private_key} ")

public_key = pow(premtive_root,private_key,finite_feild)


print(f"the public  key ----> {public_key}")

# the secound step encryption  

real_public_key =  tuple([finite_feild,premtive_root,public_key])


# ther is no problem to send the real_public_key a cross the entrent because of DLP problem
def send_the_public_key() :
   print("-"*100)
   print (f"the recever will send the publik key ----->{real_public_key}")
   print("-"*100)

send_the_public_key()


# in the side of the sender will genreate random number coprime withe q and less then q-1


def genrate__k___(f_f) :
   p_k = random.randint(2,f_f-1)
   while eclude(p_k,f_f) != 1 or not is_prime(p_k) :
      p_k = random.randint(2,f_f-1)
   return p_k

k = genrate__k___(finite_feild) # k is not neccery to be prime 


message = input("please enter your messge ")
# we will handel the case of m > f_f later ^_^
encoded_message = [ord(c) for c in message]

print("-"*100)
print(f"the encoded_message ---------> {encoded_message}")
print("-"*100)

crypted_message = []
for trunk in encoded_message :
   c1 = pow(premtive_root,k,finite_feild)
   precdence = trunk  * pow (public_key,k) # you can't achive c2 directly by donig c2 = primtive_root ^ k mode f_f
   c2 =  pow(precdence,1,finite_feild)
   crypted_trunk = tuple([c1,c2])
   crypted_message.append(crypted_trunk)

def send_cifier_text() :
   print("-"*100) 
   print(f"send the crypted message --- -> {crypted_message} ")
   print("-"*100)

send_cifier_text()

# the secound step is  the decryption 

decrepted_mesage = []
for crypted_trunk in crypted_message : 
   z = pow(crypted_trunk[0],private_key,finite_feild)
   precdence_2  = crypted_trunk[1] * pow (z,finite_feild-2)
   decrypted_trunk = pow(precdence_2,1,finite_feild)
   decrepted_mesage.append(decrypted_trunk)

print("-"*100)
print(f"the decrepted message ------> {decrepted_mesage}")
message = "".join(chr (c) for c in decrepted_mesage)
print("-"*100)
print(f"the decoded message -----> {message}")
print("-"*100)

# i was think that the Liner feadback shift register (LFSR) until i understand the elGamel and DLP problem 
# made it with love by nidhal i hope u find it helpfull my allah bless  you  and guid u in your life


