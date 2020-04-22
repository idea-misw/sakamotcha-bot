import pickle
import random
from pathlib import Path

from analyzer import Analyzer


class Generator:
    def __init__(self, ngram_size=3):
        self.ngram_size = ngram_size

        self.chain = {}
        self.init_prefix_list = []
        self.original_list = []
        
        self.analyzer = Analyzer()

        self.trial_num = 1000
        self.max_result_len = 280
        self.error_message = 'ﾀｽｹﾃｰｯｯ'
        self.symbol_list = [
            ('"', '"'), ("'", "'"), ('(', ')'),
            ('「', '」'), ('『', '』'), ('【', '】'),
            ('｢', '｣')
        ]

        self.dump_file = 'dumped_data.pickle'
    
    def load(self, file=None):
        load_p = Path(self.dump_file if file is None else file)
        with load_p.open('rb') as f:
            load_data = pickle.load(f)

        (
            self.ngram_size,
            self.chain,
            self.init_prefix_list,
            self.original_list
        ) = load_data

    def dump(self, file=None):
        dump_data = (
            self.ngram_size,
            self.chain,
            self.init_prefix_list,
            self.original_list
        )

        dump_p = Path(self.dump_file if file is None else file)
        with dump_p.open('wb') as f:
            pickle.dump(dump_data, f)

    def compute_length(self, line):
        line_len = 0
        for char in line:
            char_len = (len(hex(ord(char))) - 1) // 2
            if char_len > 2:
                char_len = 1  # emojis
            line_len += char_len
        return line_len

    def validate_symbol(self, line):
        symbol_stack = []
        for char in line:
            for l_symbol, r_symbol in self.symbol_list:
                if char == l_symbol:
                    symbol_stack.append(l_symbol)
                if char == r_symbol:
                    if not symbol_stack:
                        return False
                    top_symbol = symbol_stack.pop()
                    if top_symbol != l_symbol:
                        return False
        if symbol_stack:
            return False
        return True

    def learn(self, sentence):
        self.original_list.append(sentence)

        wakati = self.analyzer.analyze(sentence)
        wakati.append('EOS')

        for i in range(len(wakati) - self.ngram_size + 1):
            prefix = tuple(wakati[i:i+self.ngram_size-1])
            if not i:
                self.init_prefix_list.append(prefix)        
            if prefix not in self.chain:
                self.chain[prefix] = []
            self.chain[prefix].append(wakati[i+self.ngram_size-1])

    def generate(self):
        for i in range(self.trial_num):
            prefix = random.choice(self.init_prefix_list)
            result_list = list(prefix)

            midasi = random.choice(self.chain[prefix])
            while midasi != 'EOS':
                result_list.append(midasi)
                prefix = prefix[1:] + (midasi,)
                midasi = random.choice(self.chain[prefix])

            result = ''.join(result_list)
            if result in self.original_list:
                # print('Existing:', result)
                continue
            if self.compute_length(result) > self.max_result_len:
                # print('Length over:', result)
                continue
            if not self.validate_symbol(result):
                # print('Symbol invalid:', result)
                continue
            return result
        
        return self.error_message


if __name__ == '__main__':
    g = Generator(ngram_size=2)

    sample_list = [
        'サカモトなんていないのにね……',
        'みんなサカモト'
    ]
    for sample in sample_list:
        g.learn(sample)

    print(g.generate())