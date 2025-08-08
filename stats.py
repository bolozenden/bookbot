def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_freq(text):
    text = text.lower()
    char_freq = {}
    for char in text:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq

def get_sorted_list(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "num": char_dict[char]})
    sorted_list.sort(reverse=True, key=lambda d: d["num"])
    return sorted_list

