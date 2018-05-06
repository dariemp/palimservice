import argparse
import sys
from lib import PalindromeFinder, JSONFileKeyReader


def process_file(file_path):
    try:
        palindrome_finder = PalindromeFinder(JSONFileKeyReader(file_path))
        return palindrome_finder.get_palindromes()
    except FileNotFoundError:
        print('\nFile not found in the specified path: {}\n'.format(file_path), file=sys.stderr)
        exit(1)

def main():
    parser = argparse.ArgumentParser(description='Read palindromes from JSON file')
    parser.add_argument('file_path', type=str, help='patht to JSON input file')
    args = parser.parse_args()
    palindromes = process_file(args.file_path)
    print('\nPalindromes found:')
    for palindrome in palindromes:
        print(palindrome)
    print('\nNumber of palindromes found: {}\n'.format(len(palindromes)))
    exit(0)


if __name__ == '__main__':
    main()
