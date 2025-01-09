'''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91*99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
def isPalindrome(num):
    if num == int(str(num)[::-1]):
        return True
    return False

def findLargestPalindrome():
    largest_palindrome = 0
    for a in range(999, 99, -1):  # Start from 999 and go down to 100
        for b in range(a, 99, -1):  # Avoid duplicate calculations by starting from 'a'
            product = a * b
            if isPalindrome(product) and product > largest_palindrome:
                largest_palindrome = product
                mult1 = a
                mult2 = b
    return print(f"The largest palindrome made from the product of two 3-digit numbers is {largest_palindrome} = {mult1} * {mult2}")

findLargestPalindrome()

