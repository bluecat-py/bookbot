from stats import char_count, word_count, sort_dict_count
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sort_dict_count((char_count(sys.argv[1])))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(word_count(sys.argv[1]))
        print("--------- Character Count -------")
        for item in book:
            if item["char"].isalpha():
                print(f"{item["char"]}: {item["num"]}")

if __name__ == "__main__":
    main()