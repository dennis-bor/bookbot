import sys
from stats import count_words, count_chars, chars_dict_to_sorted_list

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_chars(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def print_report(book_path, num_words, symbol_dict):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for item in symbol_dict:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print(f"============= END ===============")


main()
