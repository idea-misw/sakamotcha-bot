from pyknp import Juman


class Analyzer:
    def __init__(self):
        self.jumanpp = Juman()

        self.replace_map = {'"': '’', '#': '‘'}
        self.rev_map = dict(map(reversed, self.replace_map.items()))

    def analyze(self, text):
        wakati = []

        for line in text.split('\n'):
            for sentence in line.split(' '):
                for target_symbol, sub_symbol in self.replace_map.items():
                    sentence = sentence.replace(target_symbol, sub_symbol)

                result = self.jumanpp.analysis(sentence)
                for mrph in result.mrph_list():
                    midasi = mrph.midasi
                    if midasi in self.rev_map:
                        midasi = self.rev_map[midasi]
                    wakati.append(midasi)

                wakati.append(' ')
            del wakati[-1]

            wakati.append('\n')
        del wakati[-1]

        return wakati


if __name__ == '__main__':
    a = Analyzer()
    
    sample = '"サカ モト"なんて\nいないのに#ね……'
    print(a.analyze(sample))