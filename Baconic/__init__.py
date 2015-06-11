__author__ = 'Usual'

WORD_LENGTH = 5

def split(ciphers):
    length = len(ciphers) / WORD_LENGTH
    return [ciphers[i*WORD_LENGTH:(i+1)*WORD_LENGTH] for i in range(length)]

def trans(cipher):
    dict = {'A': '0', 'B': '1', 'a' : '0', 'b': '1'}
    return chr(ord('A') + int("".join([dict[i] for i in cipher]), 2))

def decrpyt(ciphers):
    ciphers = split(ciphers)

    rtn = []

    for cipher in ciphers:
        rtn.append(trans(cipher))

    return "".join(rtn)

if __name__ == '__main__':
    print decrpyt("ABAAAABABBABAAAABABAAABAAAAAABAAAAAAAABAABBBAABBAB")