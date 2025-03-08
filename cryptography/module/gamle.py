import random
import math
from sympy import isprime, mod_inverse

class ElGamal:
   def __init__(self, key_size=256):
      """
      Initialize ElGamal cryptosystem with given key size
      
      Parameters:
      key_size (int): Size of the prime modulus in bits
      """
      self.key_size = key_size
      self.p = None  # Prime modulus
      self.g = None  # Generator
      self.a = None  # Private key
      self.h = None  # Public key
      
   def generate_prime(self, bits):
      """Generate a random prime number of specified bit length"""
      while True:
         # Generate a random odd number of the specified bit length
         p = random.getrandbits(bits) | 1
         if p.bit_length() == bits and isprime(p):
               return p
   
   def find_generator(self, p):
      """Find a generator for the cyclic group Z_p*"""
      # For simplicity, we'll just try random elements
      # In practice, there are more efficient methods
      phi = p - 1
      
      # Find the prime factors of phi
      factors = []
      # For demonstration, we'll use a simplified approach
      # In practice, we would use a more efficient factorization algorithm
      d = 2
      temp = phi
      while d * d <= temp:
         while temp % d == 0:
               if d not in factors:
                  factors.append(d)
               temp //= d
         d += 1
      if temp > 1 and temp not in factors:
         factors.append(temp)
      
      # Test random elements
      while True:
         g = random.randint(2, p-1)
         is_generator = True
         
         # Check if g^(phi/q) mod p != 1 for all prime factors q of phi
         for q in factors:
               if pow(g, phi // q, p) == 1:
                  is_generator = False
                  break
                  
         if is_generator:
               return g
   
   def generate_keys(self):
      """Generate ElGamal key pair"""
      # Generate a prime modulus
      self.p = self.generate_prime(self.key_size)
      
      # Find a generator of the multiplicative group of integers modulo p
      self.g = self.find_generator(self.p)
      
      # Choose a random private key
      self.a = random.randint(2, self.p - 2)
      
      # Compute the public key
      self.h = pow(self.g, self.a, self.p)
      
      return {
         'public_key': (self.p, self.g, self.h),
         'private_key': self.a
      }
   
   def encrypt(self, m, public_key=None):
      """
      Encrypt a message using ElGamal
      
      Parameters:
      m (int): Message to encrypt (must be < p)
      public_key (tuple): Optional external public key (p, g, h)
      
      Returns:
      tuple: Ciphertext (c1, c2)
      """
      if public_key:
         p, g, h = public_key
      else:
         p, g, h = self.p, self.g, self.h
         
      # Ensure message is in the valid range
      if m >= p:
         raise ValueError("Message must be less than p")
         
      # Choose a random k
      k = random.randint(1, p - 2)
      
      # Compute c₁ = g^k mod p
      c1 = pow(g, k, p)
      
      # Compute c₂ = m × h^k mod p
      c2 = (m * pow(h, k, p)) % p
      
      return (c1, c2)
   
   def decrypt(self, ciphertext, private_key=None, p=None):
      """
      Decrypt a ciphertext using ElGamal
      
      Parameters:
      ciphertext (tuple): Ciphertext (c1, c2)
      private_key (int): Optional external private key
      p (int): Optional prime modulus if using external private key
      
      Returns:
      int: Decrypted message
      """
      c1, c2 = ciphertext
      
      if private_key:
         a = private_key
         if not p:
               p = self.p
      else:
         a = self.a
         p = self.p
         
      # Calculate s = c₁^a mod p
      s = pow(c1, a, p)
      
      # Calculate s^(-1) mod p
      s_inv = mod_inverse(s, p)
      
      # Compute m = c₂ × s^(-1) mod p
      m = (c2 * s_inv) % p
      
      return m

# Example usage
def demo_elgamal():
   # For demonstration, use a smaller key size
   elgamal = ElGamal(key_size=64)
   
   # Generate keys
   keys = elgamal.generate_keys()
   print(f"Generated prime p: {elgamal.p}")
   print(f"Generator g: {elgamal.g}")
   print(f"Private key a: {elgamal.a}")
   print(f"Public key h = g^a mod p: {elgamal.h}")
   
   # Original message
   m = 42
   print(f"\nOriginal message: {m}")
   
   # Encrypt message
   ciphertext = elgamal.encrypt(m)
   c1, c2 = ciphertext
   print(f"Encrypted ciphertext: ({c1}, {c2})")
   
   # Decrypt message
   decrypted = elgamal.decrypt(ciphertext)
   print(f"Decrypted message: {decrypted}")
   
   # Verify encryption/decryption worked
   assert decrypted == m, "Decryption failed!"
   print("Encryption and decryption successful!")

if __name__ == "__main__":
   demo_elgamal()