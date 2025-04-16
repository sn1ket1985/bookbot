def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def get_num_words(text):
    words = text.split()
    return len(words)


def numb_char(text):
    text = text.lower()
    letter_counts = {}
    for char in text:
        lowered = char.lower()
        letter_counts[lowered] = letter_counts.get(lowered, 0) + 1
    return letter_counts

def sort_lst(text):
    letter_counts = numb_char(text)    
    char_list = [{"char": key, "count": value} for key, value in letter_counts.items()]
    char_list.sort(key=lambda x: x["count"], reverse=True)
    return char_list

   