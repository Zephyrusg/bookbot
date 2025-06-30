def get_num_words(content):
    words = content.split()
    return len(words)

def count_letters(content):
    content = content.lower()
    dict = {}
    for letter in content:
        if letter in dict:
            dict[letter] = (dict[letter]) + 1
        else: 
            dict[letter] = 1
    return dict

def sort_on(items):
    return items[1]

def sort_letter_count(dict):
    dict = sorted(dict.items(), key=sort_on, reverse=True)
    return dict
