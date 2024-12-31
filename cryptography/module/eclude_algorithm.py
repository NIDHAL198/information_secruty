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

n1=int(input("please enter the first number n1 = "))
n2=int(input("please enter the secound number n2 = "))
print(f"le pgcd de {n1} et {n2} est pgcd({n1},{n2}) = {eclude(n1,n2)}")