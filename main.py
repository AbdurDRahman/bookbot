from stats import (
    get_words_count,
    get_book_text,
    count_each_character,
    sort_on,
    convert_dictionary
)

import sys
import os 

def display(path , word_count , characters_list ):
    print("============ BOOKBOT ============")
    
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for character in characters_list:
        print(f"{character['character']}: {character['num']}")

    print ("============= END ===============")





def main():

    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    name_of_book = sys.argv[1]

    if not os.path.exists( name_of_book):
    
        print(f"Error: File '{name_of_book}' not found")
        sys.exit(1)
    
    elif not os.path.isfile(name_of_book):
    
        print(f"Error: '{name_of_book}' is not a file")
        sys.exit(1)

    text = None 
    
    try :
        text = get_book_text(name_of_book)
    except Exception as e:
        print(e)
        sys.exit(1)
    
    number = get_words_count(text)

    characters_list = convert_dictionary(count_each_character(text))
    characters_list.sort(reverse = True , key = sort_on)

    display(name_of_book , number , characters_list)


main()



