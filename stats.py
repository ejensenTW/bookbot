def read_file(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(file_contents):
    word_count = len(file_contents.split())
    return word_count

def get_letter_count(file_contents):
    split = list(file_contents.lower())
    splitdict = {}
    for letter in split:
        if letter in splitdict:
            splitdict[letter] += 1
        else:
            splitdict[letter] = 0
            splitdict[letter] += 1
    return splitdict

def sort_on(item):
    return item["num"]

def sort_letter_count(letterdict):
    count_list = []
    for entry in letterdict:
        if entry.isalpha():
            count_list.append({"char": entry, "num": letterdict[entry]})  
    count_list.sort(reverse=True, key=sort_on)
    for count in count_list:
        print(count["char"] + ": " + str(count["num"]))
    return count_list
