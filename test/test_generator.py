import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

corpus_p = Path(__file__).resolve().parents[1] / 'data' / 'sakamo_corpus.json'

import json
with corpus_p.open('r') as f:
    corpus = json.load(f)

from generator import Generator
g = Generator()

for text in corpus:
    g.learn(text)
    
for i in range(100):
    print(g.generate())