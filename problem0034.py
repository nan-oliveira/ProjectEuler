from math import factorial

# Pré-calculando os fatoriais de 0 a 9 para eficiência
factorials = {str(i): factorial(i) for i in range(10)}

def digit_factorial_sum(n):
    """Calcula a soma dos fatoriais dos dígitos de um número n"""
    return sum(factorials[d] for d in str(n))

# Estimativa do limite superior
# Para números grandes, a soma dos fatoriais dos dígitos não consegue "alcançar" o número.
# Exemplo: 7 dígitos -> 7 * 9! (2540160 é o máximo que conseguimos testar)
upper_limit = 7 * factorial(9)

# Encontrando os números curiosos
curious_numbers = []
for i in range(10, upper_limit):  # Começa em 10 porque 1 e 2 são excluídos
    if i == digit_factorial_sum(i):
        curious_numbers.append(i)

# Resultado final
print("Números curiosos:", curious_numbers)
print("Soma:", sum(curious_numbers))
