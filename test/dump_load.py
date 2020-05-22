import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

import json
from generator import Generator

p = Path(__file__).resolve().parents[1] / 'data' / 'sakamo_corpus.json'
with p.open(encoding='utf-8') as f:
    corpus = json.load(f)

g = Generator()
g.learns(corpus)

q = Path(__file__).resolve().parent / 'temp_data.pickle'
g.dump(q)

h = Generator()  # another instance
h.load(q)

for text in h.generates(10):
    print(text)
