import os
import csv
from collections import Counter

csv_path = os.path.join(
    os.path.dirname(__file__), '..', 'twitter', 'texts.csv'
)
with open(csv_path, encoding='utf-8', newline='') as f:
    corpus = [row[0] for row in csv.reader(f)]

def is_symbol(char):
    if '0' <= char <= '9':                               # digit
        return False
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':         # latin
        return False
    if 'ぁ' <= char <= 'ゖ' or 'ァ' <= char <= 'ヺ':     # kana
        return False
    if int('4e00', 16) <= ord(char) <= int('9FFF', 16):  # kanji
        return False
    if 'ｦ' <= char <= 'ﾝ':                               # halfwidth katakana
        return False
    return True

counter = Counter()

for text in corpus:
    for char in text:
        if is_symbol(char):
            counter[char] += 1

# print(counter)

symbols = sorted(counter)
print(symbols)

# print(list(map(ord, symbols)))
