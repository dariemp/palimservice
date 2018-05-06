import os
from flask import Flask, Response
from lib import PalindromeFinder, JSONFileKeyReader


app = Flask(__name__)


def _get_palindromes():
    """
    Get palindromes from the file which path is specified in the environment variable
    FLASK_INPUT_FILE_PATH. If not provided it looks for the file sample.txt in the local directory.

    Returns:
        list: A list of strings, everyone of which is a palindrome
    Raises:
        FileNotFoundError: if a file can't be found in the location provided by FLASK_INPUT_FILE_PATH
    """
    file_path = os.environ.get('FLASK_INPUT_FILE_PATH', 'sample.txt')
    palindrome_finder = PalindromeFinder(JSONFileKeyReader(file_path))
    return palindrome_finder.get_palindromes()


def palindromes_list_builder(palindromes):
    """
    Response builder that creates a text response formed by each palindrome in a new line

    Args:
        palindromes (list): A list of strings, everyone of which is a palindrome
    Returns:
        str: a text string containing each palindrome in a new line
    """
    response = ''
    for palindrome in palindromes:
        response += palindrome + '\n'
    return response


def palindromes_count_builder(palindromes):
    """
    Response builder that creates a text response containing the number of palindromes

    Args:
        palindromes (list): A list of strings, everyone of which is a palindrome
    Returns:
        str: a text string containing the number of palindromes
    """
    return str(len(palindromes))


def endpoint_handler(response_builder):
    """
    A functions that knows how to handle responses, based a different response builders

    Args:
        response_builder: a function that knows how to build a response based on a list of palindromes
    Returns:
        response: A Response object containing the data to be send to clients throught HTTP
    """
    try:
        return Response(response_builder(_get_palindromes()), content_type='text/plain; utf-8')
    except FileNotFoundError:
        return Response('Server improperly configured', status=500, content_type='text/plain; utf-8')


@app.route('/palindromes')
def get_palindromes():
    """API endpoint for returning a palindromes list"""
    return endpoint_handler(palindromes_list_builder)


@app.route('/palindromes/count')
def get_palindromes_count():
    """API endpoint for returning a palindromes count"""
    return endpoint_handler(palindromes_count_builder)
