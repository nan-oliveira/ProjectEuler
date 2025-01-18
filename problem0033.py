
def mdc(a, b):
    """
    Calcula o Máximo Divisor Comum (MDC) de dois números usando o Algoritmo de Euclides.
    """
    while b != 0:
        a, b = b, a % b  # Atualiza 'a' com 'b' e 'b' com o resto da divisão
    return a

num_mult = 1
den_mult = 1
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                num = (a*10 + b)
                den = (c*10 + d)
                frac = num / den
                possible_values = []
                if a == c:
                    possible_values.append(b/d)
                if a == d:
                    possible_values.append(b/c)
                if b == c:
                    possible_values.append(a/d)
                if b == d:
                    possible_values.append(a/c)
                if (frac in possible_values) and (frac < 1):
                    print(f'{num} / {den}')

                    num_mult = num_mult * num
                    den_mult = den_mult * den

mdc_v = mdc(num_mult, den_mult)
print('\n')
print(den_mult/ mdc_v)