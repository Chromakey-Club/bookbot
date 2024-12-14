def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count(file_contents)
        character_dictonary = sort_dictonary(each_character_count(file_contents))
        for item in character_dictonary:
            if item[0].isalpha():
                print("The", item[0], "character was found", item[1], "times")
        print("--- End report ---")

def word_count(book):
    words = len(book.split())
    print("Number of Words:", words, '\n')

def each_character_count(book):
    alphabet = {}
    new_letter = ""
    words = book.split()
    for word in words:
        for letter in word.lower():
            if letter not in alphabet.keys():
                alphabet[letter] = 1
            else:
                alphabet[letter] += 1
            new_letter = letter
    return alphabet

def sort_dictonary(dictonary):
    dictonary_list = list(dictonary.items())
    return sorted(dictonary_list, key=lambda tup: tup[1], reverse=True)

    
main()