def ceazer_shifer(text,key) :
   resualt = ""
   for char in text : 
      if char.isupper():
         resualt +=  chr((ord (char)+key + 61 )% 26 +  65 )
      elif char.islower():
         resualt += chr((ord(char) + key -97)%26  + 97)
      else : 
         resualt +=char
   return resualt



def decrypt_ceaser (msg) : 
   for key in range (0,27) :
      decrepted_msg = ""
      for char in msg:
         if char.isupper():
            decrepted_msg += chr((ord(char) - key -65)%26 + 65)
         elif char.islower():
            decrepted_msg += chr((ord(char) - key - 97)%26 + 97)
         else:
            decrepted_msg +=char
      print("-"*20)
      print(f"the key {key} ==> {decrepted_msg}")
      print("-"*20)

message = "EZSHFTD JHRR SNHKDS OKZMDS"

print(f"-------------brote force attak------ ")
decrypt_ceaser(message)


