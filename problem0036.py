def isPalindrome(num):
    if num == int(str(num)[::-1]):
        return True
    return False

def decimal_to_binary(n):
    binary = []
    while n > 0:
        binary.append(str(n % 2))  # Guarda o resto
        n = n // 2  # Atualiza o número para o quociente inteiro
    return int(''.join(binary[::-1]))

sum_value = 0
for i in range(1, 1_000_000 + 1):
    num_bin = decimal_to_binary(i)
    if isPalindrome(i) and isPalindrome(num_bin):
        sum_value += i
print(sum_value)