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


def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_on(d):
    return d["num"]

