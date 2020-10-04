# Imaginary Sakamoto Bot

Imaginary Sakamoto Bot (空想サカモトBot) is a twitter bot that tweets like [Sakamoto](https://twitter.com/sksk_sskn), a member of the 54th generation of MISW. This repository contains some codes that compose it, including Sakamoto Tweet Generator. :whale:

## Sakamoto Tweet Generator

Sakamoto Tweet Generator (サカモトツイートジェネレータ) generates a short sentence that reminds us of Sakamoto.

    >>> from generator import Generator
    >>> g = Generator()
    >>> g.load()  # load the model
    successfully loaded
    >>> g.generate()
    'ざむちゃんが1000人'

Actually, this is a *primitive* sentence generator based on morphological analysis and Markov chains. Under these two concepts, it generates a Sakamoto-like sentence by

- analyzing a number of existing Sakamoto tweets into sequences of morphemes and
- building a Markov model (trigram-based by default) with the analyzed texts.

**Note**: For the analysis of morphemes, this generator uses [Juman++](https://github.com/ku-nlp/jumanpp) via [PyKNP](https://github.com/ku-nlp/pyknp). Details of them can be found [here](http://nlp.ist.i.kyoto-u.ac.jp/index.php?NLP%E3%83%AA%E3%82%BD%E3%83%BC%E3%82%B9).

## Imaginary Sakamoto Bot

Its tweets are *protected* but if you are followed by the original, your follower request will be accepted.

**Note**: Authority to approve/deny a follower request is possessed by Sakamoto, not me.

Occurrence of its tweeting follows a Poisson distribution with a mean of 4 /day. For example, the probability of posting exactly 3 tweets in 12 hours can be calculated as 0.180.

## Related Links

- [サカモトカレンダー Advent Calendar 2019 - Adventar](https://adventar.org/calendars/4124)
    - [サカモトカレンダー結果発表 - HackMD](https://hackmd.io/@tDXhDauJRa-w18jv5uZifA/ryaR5uPkU)
    - [サカカレ、概念 - HackMD](https://hackmd.io/@kA0OlUhGRNmJkK7Nnx4QaQ/S1w1XBy0S)
- [54代の可愛い男たちで打線組んだ＋サカモト空想語録 - HackMD](https://hackmd.io/@aozam/rkFHa6HaB)
- [サカモトツイートジェネレータ - HackMD](https://hackmd.io/@UYg3xdmCSoOf6eSi_ZPkug/Skpua809S)
