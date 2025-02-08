def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_chars(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_chars(text):
    symbol_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in symbol_dict:
            symbol_dict[char] += 1
        else:
            symbol_dict[char] = 1
    return symbol_dict


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_report(book, num_words, symbol_dict):
    print(f"--- Begin report of {book} ---")
    print(f"Book has {num_words} words")
    for item in symbol_dict:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print(f"--- End report ---")


main()
