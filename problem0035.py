
def maiorFator(n):
    fator = 2  # Começamos com o menor número primo
    while fator * fator <= n:  # Verificamos até a raiz quadrada de n
        if n % fator == 0:  # Se o fator divide n
            n //= fator  # Reduzimos n (mesmo que n = n / fator)
        else:
            fator += 1  # Passamos para o próximo candidato
    return n  # O maior fator restante é o maior primo

def isPrime(n):
    if n == maiorFator(n):
        return True
    return False

def rotacoes(numero):
    """
    Retorna todas as rotações de um número.

    Parâmetros:
        numero (int): O número a ser rotacionado.

    Retorno:
        list: Uma lista com todas as rotações do número.
    """
    numero_str = str(numero)
    tamanho = len(numero_str)

    # Use uma lista por compreensão para gerar rotações
    return [int(numero_str[i:] + numero_str[:i]) for i in range(tamanho)]

def verif_list(lista):
    for val in lista:
        if not isPrime(val):
            return False
    return True

values_out = [2]
for i in range(3, 10**6 + 1, 2):
    all_rotations = rotacoes(i)
    if verif_list(all_rotations):
        values_out.append(i)

print(len(values_out))
