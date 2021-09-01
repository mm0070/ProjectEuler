# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
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

factors = []
n = 600851475143

p = 2

while n != 1:
    if n%p == 0:
        n = n/p
        factors.append(p)
        p = 2
    else:
        p = next_prime(p)

print(max(factors))