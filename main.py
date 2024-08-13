character_dict = {}
lower_case = text.lower()
sorted_dict = {}

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    num_char = get_char_count(text)
    print(f"{num_words} words found in the document")
    print(num_char)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    word_count = 0

    for word in words:
        word_count += 1
    return word_count

def get_char_count(text):

    for char in lower_case:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    
    for key in sorted(character_dict.keys()):
        sorted_dict[key] = character_dict[key]
            
    return sorted_dict

def sort_on(sorted_dict):
    return sorted_dict["num"]

def get_book_report(text):
    sorted_list = list(sorted_dict())
    sorted_list.sort(reverse=True, key=sort_on)


main()