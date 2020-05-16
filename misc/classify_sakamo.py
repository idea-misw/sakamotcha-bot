import sys
import os

from pyknp import Juman

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

half2full = str.maketrans(
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ',
    '０１２３４５６７８９ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ！”＃＄％＆’（）＊＋，－．／：；＜＝＞？＠［＼］＾＿‘｛｜｝～　'
)

jumanpp = Juman()

bert_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..',
    'data',
    'sakamoto_bert'
)

tokenizer = AutoTokenizer.from_pretrained(bert_path)
model = AutoModelForSequenceClassification.from_pretrained(bert_path)

classes = ['aozam3', 'sksk_sskn']

for line in iter(sys.stdin.readline, ''):
    result = jumanpp.analysis(line.strip().translate(half2full))
    sequence = ' '.join(mrph.midasi for mrph in result.mrph_list())

    sequence_tensor = tokenizer.encode(sequence, return_tensors='pt')
    classification_logits = model(sequence_tensor)[0]

    results = torch.softmax(classification_logits, dim=1).tolist()[0]

    print(sequence)
    for i in range(2):
        print('{}: {}'.format(classes[i], results[i]))
    print()