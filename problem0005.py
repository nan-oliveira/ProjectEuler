'''
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
 numbers from 1 to 20?
'''
def mdc(a, b):
    """
    Calcula o Máximo Divisor Comum (MDC) de dois números usando o Algoritmo de Euclides.
    """
    while b != 0:
        a, b = b, a % b  # Atualiza 'a' com 'b' e 'b' com o resto da divisão
    return a

def mmc(a, b):
    """Calcula o Mínimo Múltiplo Comum de dois números."""
    return a * b // mdc(a, b)

def menor_multiplo(n):
    """Encontra o menor número divisível por todos os números de 1 a n."""
    resultado = 1
    for i in range(1, n + 1):
        resultado = mmc(resultado, i)  # Atualiza o resultado com o MMC de resultado e i
    return resultado

# Calcula o menor múltiplo para os números de 1 a 20
n = 20
resultado = menor_multiplo(n)
print(f"O menor número divisível por todos os números de 1 a {n} é {resultado}.")