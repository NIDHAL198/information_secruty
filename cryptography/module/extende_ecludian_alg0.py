def extende_ecludain (a,b) :

   num1 = a if a > b else b 
   num2  = a if a < b else b 

   if num2 == 0 :
      return num1 , 0 ,1

   t1 = 0
   t2 = 1
   
   while num2 != 0 :
      reminder = num1%num2
      quertione  = num1 // num2
      num1 = num2
      num2 = reminder  
      t = t1  - t2 * quertione
      t1 = t2 
      t2 = t 
   pgcd = num1
   return pgcd , t2 , t1


pgcd  , x1 , x2 = extende_ecludain(120,7)
print(pgcd)
print(x1)
print(x2)

