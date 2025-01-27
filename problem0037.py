def is_prime(n):
    """Verifica se um número é primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    """Verifica se um número é primo truncável."""
    if n < 10:  # Números menores que 10 não são considerados
        return False

    # Verifica truncagem da esquerda para a direita
    num_str = str(n)
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):  # Remove dígitos da esquerda
            return False

    # Verifica truncagem da direita para a esquerda
    for i in range(len(num_str)):
        if not is_prime(int(num_str[:i+1])):  # Remove dígitos da direita
            return False

    return True

# Encontrando os 11 primos truncáveis
truncatable_primes = []
n = 11  # Começa a partir de 11, pois 2, 3, 5, e 7 são excluídos

while len(truncatable_primes) < 11:
    if is_truncatable_prime(n):
        truncatable_primes.append(n)
    n += 2  # Incrementa em 2 para verificar apenas números ímpares (exceto 2)

# Resultado final
print("Primos truncáveis:", truncatable_primes)
print("Soma:", sum(truncatable_primes))
