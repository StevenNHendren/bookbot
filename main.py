import sys
import os.path

from stats import count_words, count_characters, sort_char_dict

#infile = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        filecontents = f.read()
        return filecontents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif not os.path.exists(sys.argv[1]):
        print("Usage: python3 main.py <path_to_book>, path_to_book INVALID")
        sys.exit(1)
    else:
        infile = sys.argv[1]

    book_text = None
    book_text = get_book_text(infile)
    i = count_words(book_text)
    
    character_counts = count_characters(book_text)
    sorted_counts = sort_char_dict(character_counts)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {infile}...")
    print ("----------- Word Count ----------")
    print (f"Found {i} total words")
    print("--------- Character Count -------")
    for entry in sorted_counts:
        print(f"{entry["character"]}: {entry["count"]}")
    # print(character_counts)

main()
