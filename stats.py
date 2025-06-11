filepath = "books/frankenstein.txt"
def word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
        sentence = f"{num_words} words found in the document"
        print(sentence)
def char_count(filepath):
    char_set  = set()
    char_count = {}
    with open(filepath) as f:
        file_contents = f.read()
        for letter in file_contents:
            lower_letter = letter.lower()
            if lower_letter in char_set:
                char_count[lower_letter] +=1
            else:
                char_set.add(lower_letter)
                char_count[lower_letter] = 1
        print(char_count)

