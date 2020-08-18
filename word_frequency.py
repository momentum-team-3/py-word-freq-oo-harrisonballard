STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_contents(self):
        """
        read file contents and return as a single string
        """
        with open(self.filename, "rt") as infile:
            return infile.read()


class WordList:
    def __init__(self, text):
        # initialize list_of_words attribute
        self.text = text
        self.list_of_words = None

    def extract_words(self):
        """
        lowercases the words and strips them of punctuation
        """
        self.list_of_words = self.text.lower().replace('.', ' ').replace(',',' ').replace('!', '').split()

    def remove_stop_words(self):
        """
        after extract_words, removes all the common stop words from the list
        """
        list_with_stop_words_removed = []

        for word in self.list_of_words:
            if word not in STOP_WORDS:
                list_with_stop_words_removed.append(word)       

        self.list_of_words = list_with_stop_words_removed

    def get_freqs(self):
        """
        returns dictionary of word frequencies for FreqPrinter to use.
        Runs after extract_words and remove_stop_words.
        """
        frequencies = {}

        for word in self.list_of_words:
            #add to the counter if the word's been seen before
            if word in frequencies:
                frequencies[word] = frequencies[word] + 1
            #create a word in the dictionary if it hasn't been seen before
            else:
                frequencies[word] = 1
        return frequencies


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs

    def printfreqs(self):
        sortedfrequencies = sorted(self.freqs.items(), key=lambda x: x[1], reverse=True) 

        i = 0
        while i < 10:
            for item in sortedfrequencies:
                num_stars = sortedfrequencies[item]
                print("{sortedfrequencies} | {sortedfrequencies[value]} " + "   " + '*'*num_stars)
                i += 1

        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.
        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
