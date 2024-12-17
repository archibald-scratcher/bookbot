def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

def count_words(text):
    count = 0
    for _ in text.split():
        count += 1
    return count

main()