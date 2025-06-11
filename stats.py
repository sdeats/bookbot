filepath = "books/frankenstein.txt"
def word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
    return(num_words)
def char_count(filepath):
    char_set  = set()
    char_dict = {}
    with open(filepath) as f:
        file_contents = f.read()
        for letter in file_contents:
            lower_letter = letter.lower()
            if lower_letter in char_set:
                char_dict[lower_letter] +=1
            else:
                char_set.add(lower_letter)
                char_dict[lower_letter] = 1
    return(char_dict)
def sort_on(dict):
    return dict["num"]
def sorted_dict(filepath):
    char_dict = char_count(filepath)
    dict_list = []
    for key in char_dict:
        sort_dict = {}
        sort_dict["char"] = key
        sort_dict["num"] = char_dict[key]
        dict_list.append(sort_dict)
    dict_list.sort(reverse=True,key=sort_on)
    for group in dict_list:
        if group["char"].isalpha():
            letter = group["char"]
            number = group["num"]
            print(f"{letter}:",number)
        else:
            pass



    
