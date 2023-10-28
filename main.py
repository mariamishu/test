class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print_(self): return print(self.letters)

    def letters_num(self): return print(len(self.letters))


alph = Alphabet('english', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
alph.print_()
alph.letters_num()
