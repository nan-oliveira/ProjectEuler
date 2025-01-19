from itertools import permutations

def is_pandigital(identity):
    """
    Verifica se uma identidade (como a, b, c concatenados) é pandigital 1-9.
    """
    return sorted(identity) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def find_pandigital_products():
    """
    Encontra todos os produtos pandigitais e retorna a soma única deles.
    """
    products = set()  # Para evitar produtos duplicados

    # Gerar permutações de 1-9
    digits = '123456789'

    for perm in permutations(digits):
        # Transformar permutação em string
        perm = ''.join(perm)

        # Dividir permutação em multiplicando, multiplicador e produto
        for i in range(1, 5):  # Tamanho do multiplicando
            for j in range(i + 1, 8):  # Tamanho do multiplicador
                multiplicand = int(perm[:i])
                multiplier = int(perm[i:j])
                product = int(perm[j:])

                # Verificar a identidade
                if multiplicand * multiplier == product:
                    products.add(product)

    # Retornar a soma dos produtos únicos
    return sum(products)

# Solução
resultado = find_pandigital_products()
print(f"A soma de todos os produtos pandigitais únicos é: {resultado}")
