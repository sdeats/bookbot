def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        print(file_contents)
def word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
        sentence = f"{num_words} words found in the document"
        print(sentence)
def main(filepath):
    word_count(filepath)
main("books/frankenstein.txt")
