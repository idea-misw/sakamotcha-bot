import os
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
eval_data = []

for i in range(2):
    tsv_path = classes[i] + '_test_data.tsv'
    with open(tsv_path, encoding='utf-8') as f:
        for line in f:
            _, text = line.strip().split('\t')
            eval_data.append((i, text))

conf_mat = [[0, 0],
            [0, 0]]

for label, text in eval_data:
    result = jumanpp.analysis(text.translate(half2full))
    sequence = ' '.join(mrph.midasi for mrph in result.mrph_list())

    sequence_tensor = tokenizer.encode(sequence, return_tensors='pt')
    classification_logits = model(sequence_tensor)[0]

    results = torch.softmax(classification_logits, dim=1).tolist()[0]
    pred_label = results.index(max(results))

    conf_mat[not pred_label][not label] += 1

accuracy = sum(conf_mat[i][i] for i in range(2)) / sum(sum(row) for row in conf_mat)

precision = conf_mat[0][0] / sum(conf_mat[0])
recall = conf_mat[0][0] / sum(conf_mat[i][i] for i in range(2))

f1 = 2 * precision * recall / (precision + recall)

print('accuracy:', accuracy)
print()

print('precision:', precision)
print('recall:', recall)
print()

print('F1 score:', f1)
