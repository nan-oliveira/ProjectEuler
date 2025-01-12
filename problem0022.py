'''
<p>Using <a href="resources/documents/0022_names.txt">names.txt</a> (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.</p>
<p>For example, when the list is sorted into alphabetical order, COLIN, which is worth $3 + 15 + 12 + 9 + 14 = 53$, is the $938$th name in the list. So, COLIN would obtain a score of $938 \times 53 = 49714$.</p>
<p>What is the total of all the name scores in the file?</p>
'''

import pandas as pd
import string

file_path = '0022_names.txt'
lowercase = string.ascii_lowercase
lowercaselist = [c for c in lowercase]

with open(file_path, 'r') as file:
    line = file.readline().strip()

    processed_list = line.strip('"').split('","')

def score_name(name):
    name_lower = name.lower()
    score = 0
    for c in name_lower:
        score += lowercaselist.index(c) + 1
    return score

def calculate_score(input_list):
    input_list.sort()
    df = pd.DataFrame({})
    df['names'] = input_list
    df['position'] = list(range(1, len(input_list) + 1))
    df['score_name'] = df['names'].apply(lambda x: score_name(x))
    df['score_total'] = df['score_name'] * df['position']
    return df['score_total'].sum()

print(calculate_score(processed_list))
