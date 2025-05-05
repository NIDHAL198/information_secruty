import random

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

def generate_large_prime(min_val,max_val):
   prime = random.randint(min_val, max_val)
   while not is_prime(prime):
      prime = random.randint(min_val, max_val)
   return prime

def find_primitive_root(f_f):
   if f_f == 1:  # Special case
      return 0
   
   if f_f == 2:  # For modulo 2, 1 is the only primitive root
      return 1
   
   for candidate in range(2, f_f):
      list_generated_elements = []
      is_primitive_root = True
      
      for exp in range(1, f_f):
         el = pow(candidate, exp, f_f)
         if el in list_generated_elements:
               is_primitive_root = False
               break
         list_generated_elements.append(el)
      
      if is_primitive_root and len(list_generated_elements) == f_f - 1:
         return candidate
   
   return None 

class DiffieHellman:

   def __init__(self):
      self.p = None  # Large prime
      self.g = None  # Generator
      self.private_key = None
      self.public_key = None
      self.shared_secret = None
   
   def generate_parameters(self):
      self.p = generate_large_prime(5000,10000)
      self.g = find_primitive_root(self.p)
      return self.p, self.g
   
   def generate_keys(self):
      # Generate private key (a)
      self.private_key = random.randint(2, self.p - 2)
      
      # Calculate public key: 
      self.public_key = pow(self.g, self.private_key, self.p)
      
      return self.public_key ,self.private_key
   
   def compute_shared_secret(self, other_public_key):
      self.shared_secret = pow(other_public_key, self.private_key, self.p)
      return self.shared_secret


def simulate_key_exchange():
   dh_params = DiffieHellman()
   p, g = dh_params.generate_parameters()
   
   print(f"Common Parameters:")
   print(f"p (prime): {p}")
   print(f"g (generator): {g}")
   
   # Alice's side
   alice = DiffieHellman()
   alice.p, alice.g = p, g
   alice_public,alice_private = alice.generate_keys()

   print(f"Alice's priavte key: {alice_private}")
   print(f"Alice's public key: {alice_public}")
   
   # Bob's side
   bob = DiffieHellman()
   bob.p, bob.g = p, g
   bob_public,bob_private = bob.generate_keys()
   print(f"Bob's priavte key: {bob_private}")
   print(f"Bob's public key: {bob_public}")
   
   # Exchange public keys and compute shared secrets
   alice_shared = alice.compute_shared_secret(bob_public)
   bob_shared = bob.compute_shared_secret(alice_public)
   
   print(f"Alice's shared secret: {alice_shared}")
   print(f"Bob's shared secret: {bob_shared}")
   

if __name__ == "__main__":
   simulate_key_exchange()

