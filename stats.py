def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
    print(f"Found {num_words} total words")

def get_char_frequency(filepath):
    char_counts = {}
    with open(filepath) as f:
        file_contents = f.read().lower()
        for char in file_contents:
            if char not in char_counts:
                char_counts[char] = 1
            else:
                char_counts[char] += 1                
    return char_counts

def sort_by_count(dict):
    dict_list = []
    for key in dict:
        if key.isalpha():
            new_dict = {"char": key, "num": dict[key]}
            dict_list.append(new_dict)
    dict_list.sort(reverse=True, key= lambda x: x["num"])
    return dict_list




