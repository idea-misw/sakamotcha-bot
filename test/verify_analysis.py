import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

corpus_p = Path(__file__).resolve().parents[1] / 'data' / 'sakamo_corpus.json'

import json
with corpus_p.open('r') as f:
    corpus = json.load(f)

from analyzer import Analyzer
a = Analyzer()

failed_list = []
for text in corpus:
    wakati = a.analyze(text)
    if ''.join(wakati) != text:  # fail in restoration
        failed_list.append(text)

print(failed_list)