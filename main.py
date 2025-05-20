from stats import *
import sys

filepath = sys.argv[1]

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


tail_path = "/".join(filepath.split("/")[-2:])
contents = read_file(filepath)


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {tail_path}...")
    print('----------- Word Count ----------')
    print('Found', get_word_count(contents), 'total words')
    print('--------- Character Count -------')
    sort_letter_count(get_letter_count(contents))
    #print(type(get_letter_count(contents)))
    print('============= END ===============')

main()