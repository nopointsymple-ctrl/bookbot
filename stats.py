def get_num_words(text):

    words = text.split()
    return len(words)

def get_chars_dict(text):
    lower = text.lower()

    char_counts ={}

    for char in lower:
        char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts

def chars_dict_to_sorted_list(char_counts):
    charlist = []
    for ch, count in char_counts.items():
        charlist.append({"char": ch, "num": count})
    def sort_on(item):
        return item["num"]
    charlist.sort(reverse=True, key=sort_on)
    return charlist