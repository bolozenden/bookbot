import sys
from stats import get_num_words, get_char_frequency, sort_by_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analysing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        get_num_words(sys.argv[1])
        print("--------- Character Count -------")  
        char_counts = get_char_frequency(sys.argv[1])
        dict_list = sort_by_count(char_counts)
        for dict in dict_list:
            char = dict['char']
            count = dict['num']
            print(f"{char}: {count}")
        print("============== END ==============")

main()
