import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'generator'))

import csv
from generator import Generator

csv_path = os.path.join(
    os.path.dirname(__file__), '..', 'twitter', 'texts.csv'
)
with open(csv_path, encoding='utf-8', newline='') as f:
    corpus = [row[0] for row in csv.reader(f)]

g = Generator()
g.learns(corpus)

dump_path = os.path.join(os.path.dirname(__file__), 'temp_data.pickle')
g.dump(dump_path)

g2 = Generator()  # another instance
g2.load(dump_path)
for text in g2.generates(10):
    print(text)
