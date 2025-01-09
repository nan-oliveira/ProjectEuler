'''
<p>A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$,
 for which, $$a^2 + b^2 = c^2.$$</p>
<p>For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.</p>
<p>There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.<br>
Find the product $abc$.</p>
'''

# Encontrar o triplo de Pitágoras onde a + b + c = 1000
def find_pythagorean_triplet(sum_total):
    for a in range(1, sum_total):
        for b in range(a, sum_total - a):
            c = sum_total - a - b
            if a**2 + b**2 == c**2:
                return a, b, c

# Resolver para a soma total 1000
a, b, c = find_pythagorean_triplet(1000)
product = a * b * c
print(f"O triplo de Pitágoras é: a={a}, b={b}, c={c}")
print(f"O produto abc é: {product}")