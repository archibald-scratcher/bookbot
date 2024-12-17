def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words(file_contents)} words found in the document")
        character_counts = count_characters(file_contents)
        for character in character_counts:
            print(f"The '{character}' character was found {character_counts[character]} times")

def count_words(text):
    count = 0
    for _ in text.split():
        count += 1
    return count

def count_characters(text):
    character_counts = {}
    for character in text:
        character = character.lower()
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    return character_counts

main()