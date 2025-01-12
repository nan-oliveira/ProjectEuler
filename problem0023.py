'''
<p>A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of $28$ would be $1 + 2 + 4 + 7 + 14 = 28$, which means that $28$ is a perfect number.</p>
<p>A number $n$ is called deficient if the sum of its proper divisors is less than $n$ and it is called abundant if this sum exceeds $n$.</p>

<p>As $12$ is the smallest abundant number, $1 + 2 + 3 + 4 + 6 = 16$, the smallest number that can be written as the sum of two abundant numbers is $24$. By mathematical analysis, it can be shown that all integers greater than $28123$ can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.</p>
<p>Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.</p>
'''
divisor_cache = {}

def sum_proper_div(n):
    if n in divisor_cache:  # Verifica se já calculamos
        return divisor_cache[n]

    if n <= 1:
        return 0

    sqrt_n = int(n ** 0.5)
    divisors = set()
    for f in range(1, sqrt_n + 1):
        if n % f == 0:
            divisors.add(f)
            if f != 1 and f != n // f:
                divisors.add(n // f)

    divisor_cache[n] = sum(divisors)  # Cache do resultado
    return divisor_cache[n]

def abundant_number(inp):
    return sum_proper_div(inp) > inp

def sum_abundant_numbers(inp):
    for part1 in range(1, int(inp/2) + 1):
        part2 = inp - part1
        if abundant_number(part1) and abundant_number(part2):
            return True
    return False

def calculate_sum():
    output = 0
    for i in range(1, 28123+1):
        if not sum_abundant_numbers(i):
            output += i
    return output

print(calculate_sum())