# wellcom one more time in my simple cryptography systems ^_^
# to day we will try to so  somthing spical ---> the knapsk crypto system "____^


import random
def convert_binary(s):
   binary_text = ",".join(format(ord(char),"08b")for char in s)
   return binary_text.split(",")

message = input("please enter the message : ")
encoded_message = convert_binary(message)
encode_binary_message = []
for trunk in encoded_message : 
   for letter_binary in trunk :
      if letter_binary != " " :
         encode_binary_message.append(letter_binary)


n = len(encode_binary_message)



print(f"n = {n}")
print(f"encoded message : {encoded_message}")
print(f"encoded message : {encode_binary_message}")


#------------------- 1st step  key genration


def create_super_increasing_sequence(min):
   a_i = []
   for i in range(0,n):
      condidante_terme = random.randint(min, n) # this condition prevent us from the senarioe of chosen big number at the beging 
      if i == 0 :
         a_i.append(condidante_terme) 
      else : 
         condidante_terme = random.randint(a_i[i-1], 5 * a_i[i-1]) #each number can be greater the the peiviouse terme 5 time as max
         while sum(a_i) >= condidante_terme :# we try to respect the super increasing proprety with is a[i] > a[i-1] +a[i-2]....a[0]
            condidante_terme = random.randint(a_i[i-1], 5 * a_i[i-1]) 
         a_i.append(condidante_terme) 
   return a_i


private_key = create_super_increasing_sequence(1)
print(f"the priavte key = {private_key}")


def genrate_modulare():
   return random.randint(sum(private_key) , 10 * sum(private_key)) 

modulare = genrate_modulare()
print(f"Modulre M = {modulare}")

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


def genrate_weight ():
   w = random.randint(1 ,modulare-1)
   while eclude(modulare,w) != 1 :
      w = random.randint(1 ,modulare-1)
   return w

weight = genrate_weight()
print(f"weight W = {weight}")


def cauluc_public_key() :
   b_i = []
   for el in private_key :
      b_i.append((el * weight)%modulare)
   return b_i

public_key = cauluc_public_key()
print(f"the public key = {public_key}")


# ---------------------------------2nd step encryption
def encryption():
   cipher = 0
   for i  in range(0,n) :
      cipher += int(public_key[i] ) * int(encode_binary_message[i]) 
   return cipher

cipher = encryption()
print(f"cipher = {cipher}")


# -------------------------------3rd step decreption


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


# there is some beauty in the decrepation method *_^
def decryption():
   _,weight_inveres,_ = exetende_ecldain(modulare,weight)
   if weight_inveres < 0 :
      weight_inveres += modulare
   print(f"w_inv = {weight_inveres}")
   sum_ = (int(cipher) * int(weight_inveres) )  % modulare 
   print(f"s = {sum_}")
   message_reverse = []
   for i in range(0,n):
      if sum_ - private_key[n-i-1] >= 0 :
         sum_ -=private_key[n-i-1]
         print(True)
         
         message_reverse.append(1)
      
      else : 
         message_reverse.append(0)
         print(False)
   return message_reverse



message_encoded_decrepted = decryption()
message_encoded_decrepted.reverse()
print(message_encoded_decrepted)

tmp_str =""
message_binary_format = []
count = 0
for num in message_encoded_decrepted :
   count +=1
   tmp_str += str(num)
   if count  == 8 :
      message_binary_format.append(tmp_str)
      tmp_str = ""
      count = 0

print(message_binary_format)

message_str_format = "".join(chr(int(b,2)) for b in message_binary_format)

print(message_str_format)

# i was struglle with thies final steps *_*
# if you find this code helpfull pray allah for me  ^_^