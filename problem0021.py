'''
<p>Let $d(n)$ be defined as the sum of proper divisors of $n$ (numbers less than $n$ which divide evenly into $n$).<br>
If $d(a) = b$ and $d(b) = a$, where $a \ne b$, then $a$ and $b$ are an amicable pair and each of $a$ and $b$ are called amicable numbers.</p>
<p>For example, the proper divisors of $220$ are $1, 2, 4, 5, 10, 11, 20, 22, 44, 55$ and $110$; therefore $d(220) = 284$. The proper divisors of $284$ are $1, 2, 4, 71$ and $142$; so $d(284) = 220$.</p>
<p>Evaluate the sum of all the amicable numbers under $10000$.</p>
'''
def sum_proper_div(n):
    if n <= 1:
        return 0
    sqrt_n = int(n ** 0.5)
    divisors = []
    for f in range(1, sqrt_n + 1):
        if n % f == 0:
            divisors.append(f)
            divisors.append(int(n/f))

    divisors.remove(n)
    divisors = list(set(divisors))
    sum_out = sum(divisors)
    return sum_out

def get_sum():
    output = 0
    for i in range(1, 10_001):
        sum_v = sum_proper_div(i)
        sum_o = sum_proper_div(sum_v)
        if (sum_o == i) and (sum_o != sum_v):
            #print(i, sum_v, sum_o)
            output += i
    return output

print(get_sum())