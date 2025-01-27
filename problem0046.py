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


upper_limit = 100_000 # limitante teste
list_odd = list(range(3, upper_limit + 2, 2)) # lista de num ímpares
primes = sieve_of_eratosthenes(upper_limit) # lista de primos
composite_odd = list(set(list_odd) - set(primes)) # lista de ímpares compostos

def conjecture_Goldbach(n):
    prime_possible = [x for x in primes if x <= n]
    for pr in prime_possible:
        s_max = int(((n - pr) / 2) ** 0.5) + 1
        for s in range(1, s_max + 1):
            if n == pr + 2 * (s ** 2):
                return True
    return False

for num in composite_odd:
    if conjecture_Goldbach(num) == False:
        print(num)
        break