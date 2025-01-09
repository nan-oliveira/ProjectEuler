'''
The sum of the primes below 10
is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

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

# Exemplo de uso
n = 2_000_000  # Substitua por qualquer valor desejado
print(f"A soma dos números primos até {n}: {sum(sieve_of_eratosthenes(n))}")
