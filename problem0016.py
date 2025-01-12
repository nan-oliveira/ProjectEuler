'''
<p>$2^{15} = 32768$ and the sum of its digits is $3 + 2 + 7 + 6 + 8 = 26$.</p>
<p>What is the sum of the digits of the number $2^{1000}$?</p>
'''
num = str(2 ** 1000)
lista = [int(c) for c in num]
print(sum(lista))