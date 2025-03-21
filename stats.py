def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    char_count = {}
    
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    return char_count

def sort_on(item):
    return item[1]

def sort_dict(dict):
    count_list = list(dict.items())
    count_list.sort(reverse=True, key=sort_on)
    return count_list