import sys
from stats import word_count,char_count,sorted_dict
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        print(file_contents)
def main(filepath):
    print("======= BOOKBOT =======")
    print(f"Analyzing book found at {filepath}...")
    print("-------------- Word Count --------------")
    print(f"Found {word_count(filepath)} total words")
    print("------- Word Count -------")
    sorted_dict(filepath)
try:
    book = sys.argv[1]
except IndexError:
    print("Usage: python3 main.py <path_to_book>. Requires path to book")
    sys.exit(1)
main(book)
