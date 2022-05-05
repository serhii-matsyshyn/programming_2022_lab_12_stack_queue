"""
Palindrome class realization.
"""

from arraystack import ArrayStack  # or from linkedstack import LinkedStack


class Palindrome:
    """ Palindrome class. """

    def read_file(self, file_name):
        """ Gets list of lines from file

        :param file_name: name of file
        :type file_name: str
        :return: list of lines from file
        :rtype: list
        """

        with open(file_name, "r", encoding='utf-8') as file:
            all_lines = [line.split('/')[0].rstrip() for line in file.readlines()
                         if len(line.rstrip()) > 0]
        return all_lines

    def write_to_file(self, path: str, words: list):
        """ Writes list of words to file """
        with open(path, "w", encoding='utf-8') as file:
            for word in words:
                print(word, file=file)

    def is_palindrome(self, word: str) -> bool:
        """ Checks if word is palindrome using stack

        :param word: word to check
        :type word: str
        :return: True if word is palindrome, False otherwise
        :rtype: bool
        """
        stack = ArrayStack()
        for char in word:
            stack.push(char)
        for char in word:
            if stack.pop() != char:
                return False
        return True

    def find_palindromes(self, path_from, path_to):
        """ Finds palindromes in file

        :param path_from: path to file with words
        :type path_from: str
        :param path_to: path to file with palindromes
        :type path_to: str
        """
        words = self.read_file(path_from)
        palindromes = []
        for word in words:
            if self.is_palindrome(word):
                palindromes.append(word)
        self.write_to_file(path_to, palindromes)


if __name__ == '__main__':
    palindrome = Palindrome()
    palindrome.find_palindromes("base.lst", "palindrome_uk.txt")
    palindrome.find_palindromes("words.txt", "palindrome_en.txt")
