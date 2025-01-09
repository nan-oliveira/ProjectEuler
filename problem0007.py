'''
By listing the first six prime numbers: 2, 3, 5, 7, 11 e 13, we can see that the
6th prime is 13.

What is the 10001st prime number?
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
    if n == maiorFator(n):
        return True
    return False

cont = 0
num = 1
while cont != 10001:
    num += 1
    aux = isPrime(num)
    cont += aux
print(num)