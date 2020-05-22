import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

import json
from tokenizer import Tokenizer

corpus_p = Path(__file__).resolve().parents[1] / 'data' / 'sakamo_corpus.json'
with corpus_p.open('r') as f:
    corpus = json.load(f)

t = Tokenizer()

failed_list = []
for text in corpus:
    sequence = t.tokenize(text)
    if ''.join(sequence) != text:  # fail in restoration
        failed_list.append(text)

print(len(failed_list), 'texts cannot be restored.')
