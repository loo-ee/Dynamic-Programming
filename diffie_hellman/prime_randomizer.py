import random

def __is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_random_prime():
    while True:
        n = random.randint(1, 1000)
        if __is_prime(n):
            return n

