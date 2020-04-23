import json
from pathlib import Path

corpus_p = Path(__file__).resolve().parents[1] / 'data' / 'sakamo_corpus.json'
with corpus_p.open('r') as f:
    corpus = json.load(f)

is_symbol = lambda c: (
    not '0' <= c <= '9'  # digits
    and not ('A' <= c <= 'Z' or 'a' <= c <= 'z')  # latin
    and not ('ぁ' <= c <= 'ゖ' or 'ァ' <= c <= 'ヺ')  # kana
    and not int('4e00', 16) <= ord(c) <= int('9FFF', 16)  # kanji
    and not 'ｦ' <= c <= 'ﾝ'  # halfwidth katakana
)

symbol_set = set()
for text in corpus:
    for char in text:
        if is_symbol(char):
            symbol_set.add(char)

symbol_list = sorted(symbol_set)
print(symbol_list)

# print(list(map(ord, symbol_list)))