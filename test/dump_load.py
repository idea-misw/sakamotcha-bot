import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

import json
from generator import Generator

corpus_p = Path(__file__).resolve().parents[1] / 'data' / 'sakamo_corpus.json'
with corpus_p.open('r') as f:
    corpus = json.load(f)

g = Generator()

for text in corpus:
    g.learn(text)

dump_p = Path(__file__).resolve().parent / 'temp_data.pickle'
g.dump(dump_p)

g = Generator()  # another instance
g.load(dump_p)

for i in range(10):
    print(g.generate())