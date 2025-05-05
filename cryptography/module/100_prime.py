def is_prime(num):
    if num < 2:  
        return False
    square_root_num = int(num**0.5) + 1
    for i in range(2,square_root_num):
        if num % i == 0:  
            return False
    return True 

primes = []
number = 2 


while len(primes) < 1100:
    if is_prime(number):  
        primes.append(number)  
    number += 1 

print(primes)  
