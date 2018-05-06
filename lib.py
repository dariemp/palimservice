import json


class PalindromeFinder(object):

    def __init__(self, source_stream):
        self._source_stream = source_stream

    def _is_palindrome(self, word):
        return len(word) == 0 or (word[0] == word[-1] and self._is_palindrome(word[1:-1]))

    def get_palindromes(self):
        return [word for word in self._source_stream.readlines() if self._is_palindrome(word)]


class JSONFileKeyReader(object):

    def __init__(self, file_path):
        self._file_path = file_path

    def readlines(self):
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
