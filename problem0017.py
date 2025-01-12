'''
<p>If the numbers $1$ to $5$ are written out in words: one, two, three, four, five, then there are $3 + 3 + 5 + 4 + 4 = 19$ letters used in total.</p>
<p>If all the numbers from $1$ to $1000$ (one thousand) inclusive were written out in words, how many letters would be used? </p>
<br><p class="note"><b>NOTE:</b> Do not count spaces or hyphens. For example, $342$ (three hundred and forty-two) contains $23$
 letters and $115$ (one hundred and fifteen) contains $20$ letters. The use of "and" when writing out numbers is in compliance
   with British usage.</p>
'''
def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 1 <= n < 20:
        return ones[n]
    elif 20 <= n < 100:
        return tens[n // 10] + ones[n % 10]
    elif 100 <= n < 1000:
        return ones[n // 100] + "hundred" + ("and" + number_to_words(n % 100) if n % 100 != 0 else "")
    elif n == 1000:
        return "onethousand"
    else:
        return ""


def count_letters_in_numbers(limit):
    total_letters = 0
    for i in range(1, limit + 1):
        words = number_to_words(i)
        total_letters += len(words)
    return total_letters


# Calculate the total number of letters for numbers from 1 to 1000
total_letters = count_letters_in_numbers(1000)
print(f"Total letters used: {total_letters}")
