def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def generate_primes(lim):
    primes = []
    for n in range(2, lim + 1):
        if is_prime(n):
            primes.append(n)
    return primes

#prime numbers between 1 and 50
primes = generate_primes(50)
print("Prime numbers between 1 and 50:", primes)