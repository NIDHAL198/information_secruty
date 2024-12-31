def ceazer_shifer(text,key) :
   resualt = ""
   for char in text : 
      if char.isupper():
         resualt +=  chr((ord (char)+key + 61 )% 26 )
      elif char.islower():
         resualt += chr((ord(char) + key -97)%26  + 97)
      else : 
         resualt +=char
   return resualt
msg = "abdeAssamed23__"
crpt_msg = ceazer_shifer(msg,1)
print(crpt_msg)


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
      print(f"the key {key} ==> {decrepted_msg}")

print(f"brid force decrypted message ")
decrypt_ceaser("Cdfguucogf")


