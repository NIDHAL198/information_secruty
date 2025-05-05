import random
import numpy as np 
import matplotlib.pyplot as plt 

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

def fetch_value(FF) :
   values =  input(f"please enter the value of the Tuple(a,b) should be less then {FF} : ")
   splited_val  =  values.split(",")
   while int(splited_val[0]) >= FF or  int(splited_val[1]) >= FF : 
      values =  input(f"the value of a,b shloud be less then {FF} enter again (a,b) : ")
      splited_val  =  values.split(",")
   return int(splited_val[0]) , int(splited_val[1])

def finite_feild_genration(min_val,max_val):
   prime = random.randint(min_val, max_val)
   while not is_prime(prime):
      prime = random.randint(min_val, max_val)
   return prime

def chek_if_non_singular(FF,a,b):
   return True if (((4*pow(a,3)) + (27 *pow(b,2))) % FF == 0) else False

def matrix_construaction(FF,a,b) :
   points_matrix = np.empty((FF,3),dtype =object)
   # points_matrix.fill("None")
   points_matrix[0][0]= "X"
   points_matrix[0][1]= "y^2"
   points_matrix[0][2]= f"x^3 + {a}x + b"
   for l in range (0,FF) :
      points_matrix[l][0] = l
      points_matrix[l][1] = pow(l,2,FF)
      points_matrix[l][2] =  (pow(l,3,FF) + (a*l) + b ) % ff
   return points_matrix


def extract_point(matrix,FF) :
   point_list = []
   for l in range (0,FF) :
      for p in range(0,ff) :
         if matrix[l][2] == matrix[p][1] :
            point_list.append(tuple([l,p]))
   return point_list

def chek_belong_EC (x,y,ff,a,b) :
   return True if pow(y,2,ff) == (pow(x,3,ff) + (a*x) + b) %ff else False


def add_tow_point(p1,p2,ff,a,b) : 
   # here we have to rules when we add to point 
   # cas 1 --> P = Q 
   if p1[0] == p2[0] and p1[1] == p2[1] : 
      # cauluc lamda (slop)
      slop = (((3 * pow(p1[0],2)) + a) % ff // ((2 * p1[1]) %ff)) %ff
      x3 = (pow(slop,2,ff) - (2 * p1[0])) % ff
      y3 = ((slop * (p1[0]-x3)) -p1[1] ) % ff
      p3=(x3,y3)
      return chek_belong_EC(x3,y3,ff,a,b), p3
   # cas 2 --> P != Q 
   else : 
      slop = ((p1[1]-p2[1]) % ff // (p1[0]-p2[0])%ff) %ff
      if slop < 0 :
         slop +=ff # just the slop can not be negative the other valye (x,y) can ovissliy be negative *_^
      x3 = (pow(slop,2,ff) - ((p1[0] + p2[0])%ff)) % ff
      y3 = ((slop * (p1[0]-x3)) -p1[1] ) % ff
      p3=(x3,y3)
      return chek_belong_EC(x3,y3,ff,a,b), p3



def plot_cureve(ap,a,b) :
   x = ap[:, 0]
   y = ap[:, 1]
   print(x)

   plt.plot(x, y, color='blue', marker='o')
   plt.xlabel("X axis")
   plt.ylabel("Y axis")
   plt.title(f"y^2 = x^3 + {a}x + {b}")
   plt.grid(True)
   plt.show()




ff = finite_feild_genration(10,100)
ff=293
a,b = fetch_value(ff)
a,b = 113,25
if chek_if_non_singular(ff,a,b)  :
   print("Your curve is not non-singular")
else :
   print("-"*10)
   print(f"------------> E{ff}({a},{b})")
   print("-"*10)

   m_p = matrix_construaction(ff,a,b)
   print(m_p)

   list_points = extract_point(m_p,ff)
   print(list_points)

   array_Point = np.array(list_points)
   print(array_Point)
   plot_cureve(array_Point,a,b)


   while True:
      option = int(input("chose opration (chek_belong = 1 | add_points = 2 | exit = 3)"))
      if option == 1:
         x = int(input("x cordinate"))
         y = int(input("y cordinate"))
         if chek_belong_EC(x,y,ff,a,b) : 
            print(f"yes the point {x} , {y} belong to the eliptic curve ^_^")
         else : 
            print(f"the point {x} , {y} dosn't belomg *_*")
      if option == 2 :
         x1 = int(input("x1 cordinate"))
         y1 = int(input("y2 cordinate"))
         p1 = (x1,y1)

         x2 = int(input("x1 cordinate"))
         y2 = int(input("y2 cordinate"))
         p2 = (x2,y2)

         belong,p3 = add_tow_point(p1,p2,ff,a,b)
         print(f"the addition ---> {p1} + {p2} = {p3}")
         if belong: 
            print(f"yes the point {p3[0]} , {p3[1]} belong to the eliptic curve ^_^")
         else : 
            print(f"the point {p3[0]} , {p3[1]} dosn't belomg *_*")
         

      if option == 3:
         break


