'''
<p>A unit fraction contains $1$ in the numerator. The decimal representation of the unit fractions with denominators $2$ to $10$ are given:</p>
\begin{align}
1/2 &amp;= 0.5\\
1/3 &amp;=0.(3)\\
1/4 &amp;=0.25\\
1/5 &amp;= 0.2\\
1/6 &amp;= 0.1(6)\\
1/7 &amp;= 0.(142857)\\
1/8 &amp;= 0.125\\
1/9 &amp;= 0.(1)\\
1/10 &amp;= 0.1
\end{align}
<p>Where $0.1(6)$ means $0.166666\cdots$, and has a $1$-digit recurring cycle. It can be seen that $1/7$ has a $6$-digit recurring cycle.</p>
<p>Find the value of $d \lt 1000$ for which $1/d$ contains the longest recurring cycle in its decimal fraction part.</p>
'''

def find_recurring_cycle(d):
    """
    Calcula o comprimento da dízima periódica de 1/d.
    """
    seen_remainders = {}
    remainder = 1
    position = 0

    while remainder != 0:
        if remainder in seen_remainders:
            return position - seen_remainders[remainder]  # Comprimento do ciclo

        seen_remainders[remainder] = position
        remainder = (remainder * 10) % d
        position += 1

    return 0  # Retorna 0 se não houver dízima (decimal finito)

def find_max_d(limit=1000):
    """
    Encontra o denominador d < limit que gera a maior dízima periódica.
    """
    max_cycle_length = 0
    max_d = 0

    for d in range(1, limit + 1):
        if d % 2 != 0 and d % 5 != 0:  # Apenas valores coprimos com 10
            cycle_length = find_recurring_cycle(d)
            if cycle_length > max_cycle_length:
                max_cycle_length = cycle_length
                max_d = d

    return max_d, max_cycle_length

# Exemplo de uso
if __name__ == "__main__":
    d_max, k_max = find_max_d(1000)
    print(f"O denominador com a maior dízima periódica é {d_max}, com comprimento {k_max}.")
