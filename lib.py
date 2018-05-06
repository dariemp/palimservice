import json


class PalindromeFinder(object):
    """Given a source stream, finds lines that are palindromes"""

    def __init__(self, source_stream):
        """
        Initializes a PalindromeFinder instance with a given source stream
    
        Args:
            source_stream: a file-like object with a readlines() methods
        """
        self._source_stream = source_stream

    def _is_palindrome(self, word):
        """
        Detect if a word is a palindrome

        Args:
            word: a string to check if it is palindrome
        Returns:
            True is word is palindrom, false otherwise
        """
        return len(word) == 0 or (word[0] == word[-1] and self._is_palindrome(word[1:-1]))

    def get_palindromes(self):
        """Get all lines that are palindromes in source stream"""
        return [word for word in self._source_stream.readlines() if self._is_palindrome(word)]


class JSONFileKeyReader(object):
    """Given a file path, read lines that are JSON maps en extract data from values assigned to key \"key\""""

    def __init__(self, file_path):
        """
        Initializes a JSONFileKeyReader instance with a given file path
    
        Args:
            file_path: a path to the file that must be read
        """
        self._file_path = file_path

    def readlines(self):
        """
        Reads lines of the underlying file and parses JSON data to extract values corresponding to key \"key\".
        It works as a generator upon which it's possible to iterate.
        Raises:
            FileNotFoundError: if a file can't be found in the location provided by the file path
        """
        with open(self._file_path, 'r') as f:
            line = f.readline()
            while line:
                try:
                    data = json.loads(line)
                    word = data.get('key', None)
                    if word is not None:
                        yield word
                except (json.decoder.JSONDecodeError, AttributeError): pass
                line = f.readline()
