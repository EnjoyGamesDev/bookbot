import sys
from stats import get_num_words, get_num_characters, sort_dict


def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    sorted_count = sort_dict(num_characters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")  
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char, count in sorted_count:
        if char.isalpha() == True:
            print(f"{char}: {count}")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

        

    
main()