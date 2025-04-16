import sys
from stats import (
    get_book_text,
    get_num_words, 
    numb_char, sort_lst,
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    #path_to_file = "/home/sniket/projects/github.com/sn1ket1985/bookbot/books/frankenstein.txt" #path_to_file = "books/frankenstein.txt"  
    
    raw_text = get_book_text(path_to_file)  # Get the full text of the book
    num_words = get_num_words(raw_text)     # Count total words
    counts = numb_char(raw_text)            # Count characters, symbols, and spaces
    sorted_characters = sort_lst(raw_text)
    print_report(path_to_file, num_words, sorted_characters)
    
def print_report(path_to_file, num_words, sorted_characters):
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    for item in sorted_characters:
        if item['char'].isalpha():  # Only print letters
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")    

if __name__ == "__main__":
    main()
    