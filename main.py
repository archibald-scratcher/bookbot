def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

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