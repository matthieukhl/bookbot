def get_word_count(book):
    # convert string to list
    words = book.split()
    return len(words)

def get_book_path(path):
    with open(path) as f:
        return f.read()
    
def get_character_count(book):
    booklist = book.lower().split()
    word_count = {}
    for i in range(0, len(booklist)):
        for letter in booklist[i]:
            if letter not in word_count:
                word_count[letter] = 1
            else:
                word_count[letter] += 1
    return word_count

def get_report(word_count, character_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    
    # sort dictionary 
    sorted_dict = sorted(character_count.items(), key=lambda x:x[1], reverse=True)
    
    # iterate over list of tuples
    for character in sorted_dict:
        print(f"The '{character[0]}' character was found {character[1]} times")
    print("--- End Report ---")

def main():
    # Path to book
    path_to_file = "books/frankenstein.txt"
    
    # Open and read book
    book = get_book_path(path_to_file)
        
    # Count words
    word_count = get_word_count(book)
    
    # Count characters
    character_count = get_character_count(book)
    
    #Print report
    get_report(word_count, character_count)
    
# Call main function
if __name__ == "__main__":
    main()
    
    