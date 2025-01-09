'''
The prime factors of 13195 are 5, 7, 13 amd 29.
What is the largest prime factor of the number 600851475143?
'''

def maior_fator_primo(n):
    fator = 2  # Começamos com o menor número primo
    while fator * fator <= n:  # Verificamos até a raiz quadrada de n
        if n % fator == 0:  # Se o fator divide n
            n //= fator  # Reduzimos n (mesmo que n = n / fator)
        else:
            fator += 1  # Passamos para o próximo candidato
    return n  # O maior fator restante é o maior primo

# Testando o algoritmo
numero = 600851475143
resultado = maior_fator_primo(numero)
print(f"O maior fator primo de {numero} é {resultado}.")
