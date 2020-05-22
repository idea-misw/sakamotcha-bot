import json
from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'data' / 'sakamo_corpus.json'
with p.open(encoding='utf-8') as f:
    corpus = json.load(f)

def is_symbol(char):
    if '0' <= char <= '9':                               # digits
        return False
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':         # latin
        return False
    if 'ぁ' <= char <= 'ゖ' or 'ァ' <= char <= 'ヺ':      # kana
        return False
    if int('4e00', 16) <= ord(char) <= int('9FFF', 16):  # kanji
        return False
    if 'ｦ' <= char <= 'ﾝ':                               # halfwidth katakana
        return False
    return True

symbol_set = set()
for text in corpus:
    for char in text:
        if is_symbol(char):
            symbol_set.add(char)

symbol_list = sorted(symbol_set)
print(symbol_list)

# print(list(map(ord, symbol_list)))
