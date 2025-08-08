import sys
from stats import get_num_words, get_char_freq, get_sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        num_words = get_num_words(text)
        char_freq = get_char_freq(text)
        sorted_list = get_sorted_list(char_freq)
        print_report(sys.argv[1], num_words, sorted_list)

def get_book_text(book_path):
    with open(book_path) as b:
        book_contents = b.read()
    return book_contents

def print_report(book_path, num_words, sorted_list):
    print("=============== BOOKBOT ===============")
    print(f"Analyzing book found at {book_path}...")
    print("---------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("---------- Character Count ----------")
    for d in sorted_list:
        if d["char"].isalpha():
            print(f"{d['char']}: {d['num']}")
    print("============== END ===============")


main()