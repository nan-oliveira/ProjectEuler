p = 1000  # Limite máximo de p
dict_result = {}

# Loop para cada valor de p
for perimeter in range(1, p + 1):
    count = 0
    for a in range(1, perimeter // 2):  # a deve ser menor que p/2
        for b in range(a, (perimeter - a) // 2 + 1):  # b deve ser menor que p-a
            c = perimeter - a - b  # Calcula c diretamente
            if a**2 + b**2 == c**2:  # Verifica se é um triângulo retângulo
                count += 1
    dict_result[perimeter] = count

# Encontrar o valor de p com o maior número de soluções
max_p = max(dict_result, key=dict_result.get)  # Encontra p com maior count
max_count = dict_result[max_p]

# Exibir os resultados
print(f"O valor de p com o maior número de triângulos retângulos é {max_p}, com {max_count} triângulos.")
