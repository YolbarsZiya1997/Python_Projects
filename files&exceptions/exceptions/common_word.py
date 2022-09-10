file_name = "twenty_three_and_a_half.txt"

with open(file_name, encoding='utf-8') as f:
    contents = f.read()
    count = contents.lower().count('the ')
    print(f"The word 'the' approximately appeared {count} times in the article")