import os
from flask import Flask, Response
from lib import PalindromeFinder, JSONFileKeyReader


app = Flask(__name__)


def _get_palindromes():
    file_path = os.environ.get('FLASK_INPUT_FILE_PATH', 'sample.txt')
    palindrome_finder = PalindromeFinder(JSONFileKeyReader(file_path))
    return palindrome_finder.get_palindromes()


def palindromes_list_builder(palindromes):
    response = ''
    for palindrome in palindromes:
        response += palindrome + '\n'
    return response


def palindromes_count_builder(palindromes):
    return str(len(palindromes))


def endpoint_handler(reponse_builder):
    try:
        return Response(reponse_builder(_get_palindromes()), content_type='text/plain; utf-8')
    except FileNotFoundError:
        return Response('Server improperly configured', status=500, content_type='text/plain; utf-8')


@app.route('/palindromes')
def get_palindromes():
    return endpoint_handler(palindromes_list_builder)


@app.route('/palindromes/count')
def get_palindromes_count():
    return endpoint_handler(palindromes_count_builder)
