path = './books/frankenstein.txt'
with open(path) as f:
    file_contents = f.read()


words = {}
for letter in file_contents.lower():
    if letter not in words:
        words[letter] = 1
    else:
        words[letter] += 1 

letter_and_count = []
for item in words:
    if item.isalpha():
        letter_and_count.append((item, words[item]))



def print_log(arr = []):
    print('--- Begin report of books/frankenstein.txt ---') 
    print(f'{len(file_contents.split())} words found in the document\n')

    arr.sort()
    for tpl in arr:
        letter, count = tpl
        print(f'The {letter} character was found {count} times')

    print('\n--- End report ---')

print_log(letter_and_count)