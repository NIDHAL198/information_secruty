this code is not complete

import random


def genreate_random_prime(min_val,max_val):
   prime = random.randint(min_val, max_val)
   while not is_prime(prime):
      prime = random.randint(min_val, max_val)
   return prime

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

FF = genreate_random_prime(10,20)

def genreate_(min) :
   k = random.randint(min, FF//2)
   return k

k = genreate_(1)

print(f"the finte feild {FF}")
print(f"the saller K =  {k}")

n = int(input("please enter the number of condidate"))


while  n < k or n > FF-1 :
   n = int(input("please enter the number of condidate n should be k<= n <= q-1"))

secret = random.randint(1,FF-1)


# ---------------------1st fpase the distrbution  phase 

vect = []
for el in range(0,FF-1):
   condidate = random.randint(0,FF-1)
   vect.append(condidate)

print(len(vect) == FF-1 )


