def get_words_count(text):
    return len(text.split())

def get_book_text(file_path):
    try:
        with open(file_path) as f :
            return f.read()
    except:
        raise Exception ("Could not open file")

def count_each_character(text):
    
    char_count = {}
    for character in text :
    
        if character.lower() in char_count:
            char_count[character.lower()] += 1 
        else:
            char_count[character.lower()] = 1
    
    return char_count 

def convert_dictionary(dictionary) :
    my_dictionary_list = []
    for character in dictionary:
        if not character.isalpha() :
            continue 

        new_dictionary = {}
        new_dictionary["character"] = character 
        new_dictionary["num"] = dictionary[character]
        my_dictionary_list.append(new_dictionary)
    return my_dictionary_list

def sort_on(dictionary):
    return dictionary["num"]

    
