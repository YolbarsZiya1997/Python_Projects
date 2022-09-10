def count_words(filename):
    """Count the approximate number of words in file"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' does not exist")
        # pass if you want the program to fail silently
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file '{filename} has about {num_words} words.")


filename = ['alice.txt', 'little_women.txt', 'moby_dick.txt', 'siddhartha.txt']
for files in filename:
    count_words(files)
