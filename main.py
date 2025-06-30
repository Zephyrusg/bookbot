import sys
from stats import get_num_words
from stats import count_letters
from stats import sort_letter_count
from stats import sort_on

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    test_file_path = sys.argv[1]
    print(f"Analyzing book found at {test_file_path}..")
    print("----------- Word Count ----------")
    content_of_book = get_book_text(test_file_path)
    num_words = get_num_words(content_of_book)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    dict_letters = count_letters(content_of_book)
    sorted_dict = sort_letter_count(dict_letters)
    for k,v in sorted_dict:
        print(f"{k}: {v}")

main()