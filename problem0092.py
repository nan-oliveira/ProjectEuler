def sum_of_squares(n):
    """Calcula a soma dos quadrados dos dígitos de um número."""
    return sum(int(digit) ** 2 for digit in str(n))

def chain_destination(n, cache):
    """Determina se um número termina em 1 ou 89, utilizando cache."""
    seen = []
    while n != 1 and n != 89:
        if n in cache:
            n = cache[n]
            break
        seen.append(n)
        n = sum_of_squares(n)
    
    result = n
    for num in seen:
        cache[num] = result
    
    return result

# Cache para armazenar os resultados intermediários
cache = {}

# Contador de números que terminam em 89
count_89 = 0

# Testamos todos os números abaixo de 10 milhões
for i in range(1, 10_000_000):
    if chain_destination(i, cache) == 89:
        count_89 += 1

print(count_89)