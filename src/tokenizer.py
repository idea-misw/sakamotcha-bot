from pyknp import Juman


class Tokenizer:
    def __init__(self):
        self.jumanpp = Juman()

        self.replace_map = {'"': '’', '#': '‘'}
        self.rev_map = {s: t for t, s in self.replace_map.items()}

    def tokenize(self, text):
        sequence = []

        for line in text.split('\n'):
            for sentence in line.split(' '):
                for tgt_symbol, sub_symbol in self.replace_map.items():
                    sentence = sentence.replace(tgt_symbol, sub_symbol)

                result = self.jumanpp.analysis(sentence)
                for mrph in result.mrph_list():
                    midasi = mrph.midasi
                    if midasi in self.rev_map:
                        midasi = self.rev_map[midasi]
                    sequence.append(midasi)

                sequence.append(' ')
            del sequence[-1]

            sequence.append('\n')
        del sequence[-1]

        return sequence


if __name__ == '__main__':
    a = Tokenizer()
    
    sample = '"サカ モト"なんて\nいないのに#ね……'
    print(a.tokenize(sample))
