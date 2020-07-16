import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'generator'))

import csv
from tokenizer import Tokenizer

csv_path = os.path.join(
    os.path.dirname(__file__), '..', 'twitter', 'texts.csv'
)
with open(csv_path, encoding='utf-8', newline='') as f:
    corpus = [row[0] for row in csv.reader(f)]

t = Tokenizer()

failed_list = []
for text in corpus:
    sequence = t.tokenize(text)
    if ''.join(sequence) != text:  # fail in restoration
        failed_list.append(text)

print(len(failed_list), 'texts cannot be restored.')
