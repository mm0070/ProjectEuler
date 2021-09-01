# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
list_of_palindrome_products = []

for a in range(1, 1000):
    for b in range(1, 1000):
        n = a*b
        if str(n) == str(n)[::-1]:
            list_of_palindrome_products.append(n)

print(max(list_of_palindrome_products))