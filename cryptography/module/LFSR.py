# authore  ---> boulgamhe lahcen nidhal , zeroile abde al samad


import random


def valureInitail(degree):
   initailVAl = []
   while True :
      initailVAl = []
      for i in range(0,degree):
         initailVAl.append(random.randint(0,1))
      for u in initailVAl :
         if u :
            return initailVAl


def parse_vect(polynome):
   # polunome = polunome.strip().strip("(").rstrip(")")
   vect = [int(x) for x in polunome.split(",")]
   degree = len(vect) -1
   print("the degree inide the paerser of the pol {}",format(degree))
   return vect 


def extrat_Qs (vect,degree ,core) -> object :
   vect = vect[1:]
   cofition = []
   for el in vect :
      if el > 0 :
         cofition.append(abs(el - core))
      else :
         cofition.append(abs(el))
   return cofition


def refrence_relation(degree) :
   termes = []
   for i  in range(0,degree):
      terme = f"Un-{(degree-i)} * q{i} " 
      termes.append(terme)
   relation_refrence = " + ".join(termes)
   return relation_refrence

def caulc_tereme(indx_terme,degree,core,initailVAl,cofition):
   next_teme = 0
   update_init_val = initailVAl
   for i in  range (1,degree+1) : 
      next_teme += initailVAl[indx_terme -i -1] * cofition[degree -i]
      next_teme %= core
   update_init_val.append(next_teme)
   return next_teme,update_init_val


def caulc_sequence(degree,core,initailVAl,cofictiont):
   sequnce = []
   update_init_val = initailVAl
   for el in initailVAl :
      sequnce.append(el)
   for i in range(degree,((core**degree)-1)*2): # i make the periode equile to 2 for the user to see the reption of the terme
      next_terme,update_init_val = caulc_tereme(i,degree,core,update_init_val,cofictiont)
      sequnce.append(next_terme)
   return sequnce


if __name__ == "__main__" :

   core = int(input("please enter the feild"))
   print(f"\t\t------> the feild is {core}")
   degree = int(input("please enter the degree \n"))
   valureInitail = valureInitail(degree)

   print(valureInitail)
   polunome = input("please enter u polynome (1,0,0)\n")
   vect = parse_vect(polunome)
   print(vect)
   cofictiont = extrat_Qs(vect,degree,core)
   print(f"the cofiion {cofictiont}")
   print(refrence_relation(degree))
   print("\n\n")
   print("-"*100)
   print("------------------------LFSR sequence---------------")
   print(caulc_sequence(degree,core,valureInitail,cofictiont))
   print("-"*100)
   