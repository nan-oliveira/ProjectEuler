# Função para calcular a soma das potências quintas dos dígitos de um número
def sum_of_fifth_powers(num):
    return sum(int(digit) ** 5 for digit in str(num))

# Determinar o limite superior
# n * 9^5 precisa ser menor que o menor número com (n + 1) dígitos
power = 5
limit = 1
while limit <= 9**power * len(str(limit)):
    limit = limit * 10

# Encontrar os números que atendem à condição
results = []
for num in range(2, limit):
    if num == sum_of_fifth_powers(num):
        results.append(num)

# Soma dos números encontrados
result_sum = sum(results)
results, result_sum