import random
import numpy as np 

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

# a finite feild (Z/PZ) can be a primtve number or 2^primitve number ex:(2^3) accordeing to the noue therorem
def finite_feild_genration(min_val,max_val):
   prime = random.randint(min_val, max_val)
   while not is_prime(prime):
      prime = random.randint(min_val, max_val)
   return prime 

def chek_if_non_singular(FF,a,b):
   return True if (((4*pow(a,3)) + (27 *pow(b,2))) % FF == 0) else False

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


def genrate_a_b(ff) :
   a = random.randint(2,ff-1)
   b = random.randint(2,ff-1)
   # there is no constrine to GCD(ff,a) = 1 the onlay constrinte is that  the eliptic cureve is non-singular
   while chek_if_non_singular(ff,a,b) :
      a = random.randint(2,ff-1)
      b = random.randint(2,ff-1)
   return a,b


ff = finite_feild_genration(200,1000)
a,b = genrate_a_b(ff)



message = input("please enter your messge ")
encoded_message = [ord(c) for c in message]
print(encoded_message)

# ------------------------step 01 encode the message to EC points 

def matrix_construaction(FF,a,b) :
   points_matrix = np.empty((len(encoded_message),3),dtype =object)
   # points_matrix.fill("None")
   points_matrix[0][0]= "X"
   points_matrix[0][1]= "y^2"
   points_matrix[0][2]= f"x^3 + {a}x + {b}"
   for l in range (0,len(encoded_message)) :
      points_matrix[l][0] = int(encoded_message[l])
      points_matrix[l][1] = pow(int(encoded_message[l]),2,FF)
      points_matrix[l][2] =  (pow(int(encoded_message[l]),3,FF) + (a * int(encoded_message[l])) + b ) % ff
   return points_matrix

# i think this  is optimal soultion (space , time complxity)  beacause it  based on slove the equation  not breing all the value and mach it 
def extract_point(matrix,FF) :
   point_list = set()
   # solve the equation y^2 = x^3 + ax +b ---> it means we will serch wich y from 1 to finite feild - 1 that eaqual to x^3 + ax +b
   for l in range (0,len(encoded_message)) :
      for considant_y in range(0,FF):
         if pow(considant_y,2,FF) == matrix[l][2] : # matrix[l][2] same as  x^3 +ax+b
         # now directly i concluse the value of y wich is ---->considant_y
            point_list.add(tuple([matrix[l][0],considant_y])) # (x,y)
   return list(point_list)

p_m = matrix_construaction(ff,a,b)
print("-"*100)
print(p_m)
points = extract_point(p_m,ff)
print("-"*100)
print(points)

#-------------------- step 02 genrate the public and priavte key 
def chek_belong_EC (x,y,ff,a,b) :
   return True if pow(y,2,ff) == (pow(x,3,ff) + (a*x) + b) %ff else False


# print("Number of points on the curve:", N)
def cauluc_ADD_opreation(p1,p2,ff,a,b) : 
   # here we have to rules when we add to point 
   # cas 1 --> P = Q 
   if p1[0] == p2[0] and p1[1] == p2[1] : 
      _,mul_inv,_ = exetende_ecldain(ff,2 * p1[1]) 
      if mul_inv < 0 :
         mul_inv += ff
      # cauluc lamda (slop)
      slop = (((3 * pow(p1[0],2)) + a) % ff * mul_inv) %ff
      x3 = (pow(slop,2,ff) - (2 * p1[0])) % ff
      y3 = ((slop * (p1[0]-x3)) -p1[1] ) % ff
      p3=(x3,y3)
      return  p3
   # cas 2 --> P != Q 
   else : 
      _,mul_inv,_ = exetende_ecldain(ff,p1[0]-p2[0]) 
      if mul_inv < 0 :
         mul_inv += ff
      slop = ((p1[1]-p2[1]) % ff * mul_inv) %ff
      if slop < 0 :
         slop +=ff # just the slop can not be negative the other valye (x,y) can ovissliy be negative *_^
      x3 = (pow(slop,2,ff) - ((p1[0] + p2[0])%ff)) % ff
      y3 = ((slop * (p1[0]-x3)) -p1[1] ) % ff
      p3=(x3,y3)
      return  p3

def chose_genratore_point(ff,a,b):
   x = random.randint(2,ff-1)
   y = random.randint(2,ff-1)
   g = x,y
   while not chek_belong_EC(x,y,ff,a,b) : 
      x = random.randint(2,ff-1)
      y = random.randint(2,ff-1)
      g = x,y
   return  g

G = chose_genratore_point(ff,a,b,)
print("the genreatore ------> ",G)



def genrate_priavte_key (FF) :
   p_k = random.randint(2,FF-1)
   return p_k


#  i think the recursseve way  more  better then the  iterative way
def cauluc_MUL_opreation(G,n,ff,a,b) :
   n-=1
   G_prime = G
   # here we have to rules when we add to point in EC
   # cas 1 --> P = Q 
   for i in range(0,n):
      if G[0] == G_prime[0] and G[1] == G_prime[1] : 
         _,mul_inv,_ = exetende_ecldain(ff,2 * G[1]) 
         if mul_inv < 0 :
            mul_inv += ff
         # cauluc lamda (slop)
         slop = (((3 * pow(G[0],2)) + a) % ff * mul_inv) %ff
         x3 = (pow(slop,2,ff) - (2 * G[0])) % ff
         y3 = ((slop * (G[0]-x3)) -G[1] ) % ff
         G_prime=(x3,y3)
      # cas 2 --> P != Q 
      else : 
         _,mul_inv,_ = exetende_ecldain(ff,G[0]-G_prime[0]) 
         if mul_inv < 0 :
            mul_inv += ff
         slop = ((G[1]-G_prime[1]) % ff * mul_inv) %ff
         if slop < 0 :
            slop +=ff # just the slop can not be negative the other valye (x,y) can ovissliy be negative *_^
         x3 = (pow(slop,2,ff) - ((G[0] + G_prime[0])%ff)) % ff
         y3 = ((slop * (G[0]-x3)) -G[1] ) % ff
         G_prime=(x3,y3)
   return G_prime



n = genrate_priavte_key(ff)

public_key = cauluc_MUL_opreation(G,n,ff,a,b) # n*G is it the same of add G  n time 

print("-"*100)
print("---------------------ECC paramters---------")
print(f"------------> E{ff}({a},{b})")
print(f"genratore point G {G}")
print(f"private key  {n}")
print(f"Public key  {public_key}")
print("-"*100)

# -----------------------step 03 perforeme the encryption using reciever public key

def genrate_random_k (FF) :
   p_k = random.randint(2,FF-1)
   return p_k

k = genrate_random_k(ff)


# c =(c1,c2)
# c1 = k * G 
# c2 = m + k *public_Key
crypted_encoded_message = []
for trunk in points :
   print("------------------------",trunk)
   c1 = cauluc_MUL_opreation(G,k,ff,a,b)
   c2 = cauluc_ADD_opreation(trunk,cauluc_MUL_opreation(public_key,k,ff,a,b),ff,a,b)
   crypted_trunk= (c1,c2)
   crypted_encoded_message.append(crypted_trunk)
print(f"the encode of the crepted  message {crypted_encoded_message}")
print("-"*100)


cipher_item = []
for  trunk in crypted_encoded_message :
   for el in trunk : 
      cipher_item.append(el[0])
      cipher_item.append(el[1])
crepted_message = "".join(chr(item) for item  in cipher_item)
print(f"the crepted message  {crepted_message}")
print("-"*100)

#------------------------ step 4 performe the decreption process
# m = c2 - (n*c1)
decrepted_encoded_points = []
for crypted_trunk in crypted_encoded_message : 
   print(crypted_trunk)
   dc1 = cauluc_MUL_opreation(crypted_trunk[0],n,ff,a,b)
   dc1_ = list(dc1) # to allow affectation
   dc1_[1] *= -1 # p(x,y)----> -p (x,-y)

   decrepted_trunk = cauluc_ADD_opreation(crypted_trunk[1],dc1_,ff,a,b)
   decrepted_encoded_points.append(decrepted_trunk)
print(f"the decrepted encoded points --> {decrepted_encoded_points}")
print("-"*100)  

