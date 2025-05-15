
z=int(input("Till what we need prime fuctions for:"))

p=int(input("From where we need start prime fuctions for:"))

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def generate_primes(lim):
    primes = []
    for n in range(p, lim + 1):
        if is_prime(n):
            primes.append(n)
    return primes


primes = generate_primes(z)
print(f"Prime numbers between {p} and {z} :", primes)