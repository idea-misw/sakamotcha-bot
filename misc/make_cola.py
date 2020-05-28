from pyknp import Juman

half2full = str.maketrans(
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ',
    '０１２３４５６７８９ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ！”＃＄％＆’（）＊＋，－．／：；＜＝＞？＠［＼］＾＿‘｛｜｝～　'
)
jumanpp = Juman()

classes = [
    'aozam3',
    'sksk_sskn'
]
dev_freq = 10

train_data = []
dev_data = []

for i, class_ in enumerate(classes):
    tsv_path = class_ + '_data.tsv'
    with open(tsv_path, 'r') as f:
        for j, line in enumerate(f):
            id_str, text = line.strip().split('\t')
            full_text = text.translate(half2full)

            result = jumanpp.analysis(full_text)
            sequence = ' '.join(mrph.midasi for mrph in result.mrph_list())

            cola_row = (
                id_str,
                str(i),
                '' if i else '*',
                sequence
            )

            if j % dev_freq:
                train_data.append(cola_row)
            else:
                dev_data.append(cola_row)

with open('train.tsv', 'w') as f:
    f.write('\n'.join('\t'.join(line) for line in sorted(train_data)))

with open('dev.tsv', 'w') as f:
    f.write('\n'.join('\t'.join(line) for line in sorted(dev_data)))
