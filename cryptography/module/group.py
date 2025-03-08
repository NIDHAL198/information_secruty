
class Group  :

   def __init__(self , my_set ,  law) :
      self.my_set =  my_set
      self.law = law

   def is_group (group) :
      resualt = 0 
      list_resualt = []
      if group.law == '%' :
         elemnts = list(group.my_set)
         for el_1 in elemnts :
            for el_2 in elemnts :
               if el_2 != 0 :
                  resualt = el_1 % el_2
                  list_resualt.append(resualt)
         for e in list_resualt:
            if not  e in elemnts :
               print("this is not a valide group ")
               return
         print ("valide group")




elments = set([0,1,2,3,4])
law = '%'
g_1 = Group(elments , law)
g_1.is_group()