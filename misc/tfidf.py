import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'generator'))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# from tokenizer import Tokenizer
from generator import Generator

dump_path = os.path.join(
    os.path.dirname(__file__),
    '..',
    'test',
    'temp_data.pickle'
)

# t = Tokenizer()

g = Generator()
g.load(dump_path)

corpus = g.generates(20)
# corpus.append('外寒すぎてデッケェ冷えピタに包まれたときと全く同じ気持ちになった')
corpus.append('ざむちゃん実は戦隊モノの黄色を担当しているんだよね')

# vectorizer = TfidfVectorizer(tokenizer=t.tokenize)
vectorizer = TfidfVectorizer(analyzer='char')
X = vectorizer.fit_transform(corpus)

print(corpus[cosine_similarity(X)[-1, :-1].argmax()])
