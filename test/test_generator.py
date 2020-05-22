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
for text in g.generates():
    print(text)
