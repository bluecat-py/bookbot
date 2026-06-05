from typing import TypedDict

class CharacterCount(TypedDict):
    char: str
    num: int


def get_file_access(filepath: str):
    with open(filepath, encoding="utf-8") as f:
        file = f.read()
    return file

def word_count(filepath: str):
    words = get_file_access(filepath)
    words = words.split()
    return len(words)

def char_count(filepath: str) -> dict[str, int]:
    chars = get_file_access(filepath).lower()
    char_count = {}
    for char in chars:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_here(CharacterCount):
    return CharacterCount["num"]

def sort_dict_count(char_count):
    CharacterCount = []
    char = ""
    num = 0
    for key in char_count:
        char = key
        num = char_count[key]
        CharacterCount.append({"char": char, "num": num})
    CharacterCount.sort(reverse=True, key= sort_here)
    return CharacterCount

