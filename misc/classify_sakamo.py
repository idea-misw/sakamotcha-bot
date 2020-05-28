import sys

from pyknp import Juman

import torch
from transformers import BertTokenizer, BertForSequenceClassification

half2full = str.maketrans(
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ',
    '０１２３４５６７８９ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ！”＃＄％＆’（）＊＋，－．／：；＜＝＞？＠［＼］＾＿‘｛｜｝～　'
)
jumanpp = Juman()

bert_path = sys.argv[1]

tokenizer = BertTokenizer.from_pretrained(bert_path)
model = BertForSequenceClassification.from_pretrained(bert_path)

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