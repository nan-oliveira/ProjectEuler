from fractions import Fraction

def continued_fraction(n):
    result = 1
    for _ in range(n):
        result = 1 + Fraction(1, result + 1)
    return result

# Número de iterações para reproduzir os termos exibidos na imagem
num_terms = 1_000

# Cálculo e exibição dos resultados
count = 0
for i in range(1, num_terms):
    frac = continued_fraction(i)
    if len(str(frac.numerator)) > len(str(frac.denominator)):
        count += 1
print(count)