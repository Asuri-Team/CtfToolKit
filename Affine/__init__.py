__author__ = 'Usual'

class Affine(object):
    '''
        Class declare as a Affine instance.

        Example:

        >>> affine = Affine()
        >>> cipher = affine.encode('HelloWorld')
        >>> print cipher
    '''

    def encode(self, plain, key):
        pass

    def decode(self, cipher, key):
        pass

    def violent(self, cipher):
        pass

    def char2code(self, char):
        if not self.isAlpha(char):
            print "'%c'(0x%x) is not expected value." % (char, ord(char))
            return False

        return (ord(char.upper()[0]) - ord('A')) % 26

    def code2char(self, code):
        pass

    def isAlpha(self, char):
        return (('a' <= char <= 'z') or ('A' <= char <= 'Z'))

if __name__ == '__main__':
    affine = Affine()

    print affine.char2code('d')