# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def next_prime(i):
    i += 1
    while not is_prime(i):
        i += 1
    return i

def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

found_primes = []
n = 2

while len(found_primes) < 10001:
    if is_prime(n):
        found_primes.append(n)
    n+=1

print(len(found_primes))
print(found_primes[-1])

