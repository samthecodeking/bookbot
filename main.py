def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_dict = get_char_count(text)
    char_dict_sorted = char_dict_to_sorted_list(char_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    
    for i in char_dict_sorted:
        print(f"The '{i['Char']}' character was found {i['num']} times")
    
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    character_dict = {}
    lower_case = text.lower()
    # sorted_dict = {}
    for char in lower_case:
        if char.isalpha(): #checks if char is alphabetic
            if char in character_dict:
                character_dict[char] += 1
            else:
                character_dict[char] = 1
    
    return character_dict

    # for key in sorted(character_dict.keys()):
    #     sorted_dict[key] = character_dict[key]
            
    # return sorted_dict

def sort_on(dict):
    return dict["num"]

def char_dict_to_sorted_list(num_char_dict):
    sorted_list = []
    for i in num_char_dict:
        sorted_list.append({"Char": i , "num": num_char_dict[i]})
    sorted_list.sort(reverse=True, key=sort_on)

    return (sorted_list)

main()