import re


class Anagramator:

    anagrame = dict()

    def __init__(self, file):
        self.file = file

    def h(self, word):
        return ''.join(sorted(word))

    def read_content(self):
        with open(self.file, 'r') as fin:
            self.file_content = ''.join(fin.readlines())

    def process(self):
        self.file_content = filter(lambda v: v is not '', re.split("[, \-!?.:\n]+", self.file_content))
        for word in self.file_content:
            key = Anagramator(self.file).h(word)
            self.anagrame[key] = self.anagrame.get(key, 0) + 1
        return self.anagrame


def main():

    filename = input("Enter file name: ")
    file = Anagramator(filename)
    file.read_content()
    processed = file.process()


    while True:
        word = input('Enter the word you\'d like to look up anagrams for. Hit \'!\' to exit : ')
        if word == '!':
            break
        print('There are %s occurrences for this anagram.' % str(processed.get(file.h(word), 0)))


if __name__ == "__main__":
    main()
