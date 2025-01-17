'''
<p>Euler discovered the remarkable quadratic formula:</p>
<p class="center">$n^2 + n + 41$</p>
<p>It turns out that the formula will produce $40$ primes for the consecutive integer values $0 \le n \le 39$. However, when $n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41$ is divisible by $41$, and certainly when $n = 41, 41^2 + 41 + 41$ is clearly divisible by $41$.</p>
<p>The incredible formula $n^2 - 79n + 1601$ was discovered, which produces $80$ primes for the consecutive values $0 \le n \le 79$. The product of the coefficients, $-79$ and $1601$, is $-126479$.</p>
<p>Considering quadratics of the form:</p>
<blockquote>
$n^2 + an + b$, where $|a| &lt; 1000$ and $|b| \le 1000$<br><br><div>where $|n|$ is the modulus/absolute value of $n$<br>e.g. $|11| = 11$ and $|-4| = 4$</div>
</blockquote>
<p>Find the product of the coefficients, $a$ and $b$, for the quadratic expression that produces the maximum number of primes for consecutive values of $n$, starting with $n = 0$.</p>
'''

def maiorFator(n):
    fator = 2  # Começamos com o menor número primo
    while fator * fator <= n:  # Verificamos até a raiz quadrada de n
        if n % fator == 0:  # Se o fator divide n
            n //= fator  # Reduzimos n (mesmo que n = n / fator)
        else:
            fator += 1  # Passamos para o próximo candidato
    return n  # O maior fator restante é o maior primo

def isPrime(n):
    if n < 2:
        return False
    if n == maiorFator(n):
        return True
    return False

def sieve_of_eratosthenes(n):
    """
    Implementa o Crivo de Eratóstenes para encontrar todos os números primos até n.

    :param n: Limite superior (inclusivo) para encontrar números primos
    :return: Lista de números primos até n
    """
    # Passo 1: Criar uma lista booleana para marcar se o número é primo
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 e 1 não são primos

    # Passo 2: Iterar a partir do primeiro número primo, 2
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            # Marcar todos os múltiplos de i como não primos
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # Passo 3: Retornar os números marcados como primos
    return [x for x in range(n + 1) if primes[x]]

b_pos_values = sieve_of_eratosthenes(1000)

amount = 0
for b in b_pos_values:
    for a in range(-b, 1000):
        pos_prime = 2
        n = 0
        while isPrime(pos_prime):
            pos_prime = n ** 2 + a*n + b
            n += 1
        if n > amount:
            a_max = a
            b_max = b
            amount = n
print(a_max*b_max)
