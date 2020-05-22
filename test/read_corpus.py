import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

corpus_name = 'sakamo_corpus.json'

import json
corpus_path = Path(__file__).resolve().parents[1] / 'data' / corpus_name
with corpus_path.open(encoding='utf-8') as f:
    corpus = json.load(f)
