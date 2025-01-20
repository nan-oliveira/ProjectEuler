def count_ways_to_make_change(target, coins):
    # Inicializa um array com zeros para armazenar as combinações
    ways = [0] * (target + 1)
    ways[0] = 1  # Apenas 1 forma de fazer 0 (não usar moedas)

    # Itera por cada moeda
    for coin in coins:
        for j in range(coin, target + 1):
            ways[j] += ways[j - coin]
            #print('Coin: ', coin, 'j: ', j, 'ways[j]', ways[j])

    return ways[target]

# Definição do problema
target = 200  # £2 em pence
coins = [1, 2, 5, 10, 20, 50, 100, 200]

# Calcula o número de combinações
result = count_ways_to_make_change(target, coins)
print(f"Number of ways to make £2: {result}")