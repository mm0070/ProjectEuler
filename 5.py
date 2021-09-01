# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import sys

n = 1
while True:
    n += 1
    for i in range(1, 21):
        if n%i != 0:
            break
        if i == 20:
            print(n)
            sys.exit(0)
