import string
import pandas as pd

# alphabet
alphabet = [c for c in string.ascii_lowercase]

# read base
file_path = '0042_words.txt'
with open(file_path, 'r') as file:
    line = file.readline().strip()

    processed_list = line.strip('"').split('","')

def score_name(name):
    name_lower = name.lower()
    score = 0
    for c in name_lower:
        score += alphabet.index(c) + 1
    return score

def tn(n):
    return int(0.5 * n * (n + 1))



df = pd.DataFrame()
df['names'] = processed_list
df['score_name'] = df['names'].apply(lambda x: score_name(x))

max_score = df['score_name'].max()
list_triangle_numbers = [tn(a) for a in range(1, max_score)]

df['indicator'] = df['score_name'].isin(list_triangle_numbers)
print(df.loc[df['indicator'] == True].shape)