import json

import os
import click
from flask import Flask, Response
from lib import PalindromeFinder, JSONFileKeyReader


app = Flask(__name__)

def buid_response(palindromes):
    response = ''
    for palindrome in palindromes:
        response += palindrome + '\n'
    return response

@app.route('/palindromes')
def get_palindromes():
    file_path = os.environ.get('FLASK_INPUT_FILE_PATH', 'sample.txt')
    try:
        palindrome_finder = PalindromeFinder(JSONFileKeyReader(file_path))
        palindromes = palindrome_finder.get_palindromes()
        return Response(buid_response(palindromes), content_type='text/plain; utf-8')
    except FileNotFoundError:
        return Response('Server improperly configured', status=500, content_type='text/plain; utf-8')


@app.route('/palindromes/count')
def get_palindromes_count():
    file_path = os.environ.get('FLASK_INPUT_FILE_PATH', 'sample.txt')
    try:
        palindrome_finder = PalindromeFinder(JSONFileKeyReader(file_path))
        palindromes = palindrome_finder.get_palindromes()
        return Response(str(len(palindromes)), content_type='text/plain; utf-8')
    except FileNotFoundError:
        return Response('Server improperly configured', status=500, content_type='text/plain; utf-8')
