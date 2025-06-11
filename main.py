from stats import word_count,char_count,sorted_dict
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        print(file_contents)
def main(filepath):
    print("======= BOOKBOT =======")
    print(f"analyzing book found at {filepath}...")
    print("-------------- Word Count --------------")
    print(f"found {word_count(filepath)} total words")
    print("------- Word Count -------")
    sorted_dict(filepath)
main("books/frankenstein.txt")
