from stats import word_count,char_count
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        print(file_contents)
def main(filepath):
    char_count(filepath)
main("books/frankenstein.txt")
