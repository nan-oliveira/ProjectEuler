'''
<p>The following iterative sequence is defined for the set of positive integers:</p>
<ul style="list-style-type:none;">
<li>$n \to n/2$ ($n$ is even)</li>
<li>$n \to 3n + 1$ ($n$ is odd)</li></ul>
<p>Using the rule above and starting with $13$, we generate the following sequence:
$$13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1.$$</p>
<p>It can be seen that this sequence (starting at $13$ and finishing at $1$) contains $10$ terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at $1$.</p>
<p>Which starting number, under one million, produces the longest chain?</p>
<p class="note"><b>NOTE:</b> Once the chain starts the terms are allowed to go above one million.</p>
'''

def tamanho_cadeia(valor_inicial):
    if valor_inicial <= 1:
        return 1

    if valor_inicial % 2 == 0:
        return 1 + tamanho_cadeia(valor_inicial/2)
    return 1 + tamanho_cadeia(3*valor_inicial + 1)

tamanho_list = [0] * 1_000_001
for i in range(1, 1_000_001):
    tamanho_list[i] = tamanho_cadeia(i)

print(tamanho_list.index(max(tamanho_list)))