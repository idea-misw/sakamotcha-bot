import pickle
import random
from pathlib import Path

from tokenizer import Tokenizer


class Generator:
    def __init__(self, ngram_size=3):
        self.ngram_size = ngram_size

        self.originals = []
        self.chain = {}
        
        self.tokenizer = Tokenizer()

        self.trial_num = 1000
        self.max_result_len = 280
        self.error_message = 'ﾀｽｹﾃｰｯｯ'
        self.pair_symbols = [
            ('"', '"'),
            ("'", "'"),
            ('(', ')'),
            ('「', '」'),
            ('『', '』'),
            ('【', '】'),
            ('｢', '｣')
        ]
        self.sos_symbol = 'SOS'
        self.eos_symbol = 'EOS'

        self.dump_path = 'dumped_data.pickle'
    
    def load(self, file_path=None):
        load_p = Path(self.dump_path if file_path is None else file_path)
        with load_p.open('rb') as f:
            load_data = pickle.load(f)

        self.ngram_size, self.original_list, self.chain = load_data

    def dump(self, file_path=None):
        dump_data = (
            self.ngram_size,
            self.originals,
            self.chain
        )

        dump_p = Path(self.dump_path if file_path is None else file_path)
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
            for l_symbol, r_symbol in self.pair_symbols:
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

    def learn(self, text):
        self.originals.append(text)

        sequence = [
            self.sos_symbol,
            *self.tokenizer.tokenize(text),
            self.eos_symbol
        ]

        for i in range(len(sequence) - self.ngram_size + 1):
            prefix = tuple(sequence[i:i+self.ngram_size-1])
            if prefix not in self.chain:
                self.chain[prefix] = []
            self.chain[prefix].append(sequence[i+self.ngram_size-1])

    def learns(self, texts):
        for text in texts:
            self.learn(text)

    def generate(self):
        start_prefixes = [p for p in self.chain if p[0] == self.sos_symbol]
        for i in range(self.trial_num):
            prefix = random.choice(start_prefixes)
            sequence = list(prefix[1:])

            token = random.choice(self.chain[prefix])
            while token != 'EOS':
                sequence.append(token)
                prefix = prefix[1:] + (token,)
                token = random.choice(self.chain[prefix])

            text = ''.join(sequence)
            if text in self.originals:
                # print('Existing:', result)
                continue
            if self.compute_length(text) > self.max_result_len:
                # print('Length over:', result)
                continue
            if not self.validate_symbol(text):
                # print('Symbol invalid:', result)
                continue
            return text
        
        return self.error_message
    
    def generates(self, gen_num=100):
        return [self.generate() for i in range(gen_num)]


if __name__ == '__main__':
    g = Generator(ngram_size=2)

    sample_list = [
        'サカモトなんていないのにね……',
        'みんなサカモト'
    ]
    for sample in sample_list:
        g.learn(sample)

    print(g.generate())
