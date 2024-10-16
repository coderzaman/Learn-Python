import os

words_count = {}
search_words =  ["Python", "C", "OOP", "Hello", "Java"]

if os.path.isfile('input.txt'):
    with open('input.txt', 'r') as file:
        # Convert each line to list item
        line_list = [line.strip() for line in file]

        # store searching word as key no occurrence as value in dictionary
        words_count = {word:line_list.count(word) for word in search_words}
else:
    print("File not Exist")

# Print word and no of occurrence in file with stored dictionary
for word, count in words_count.items():
    print(f'{word} -> {count}')