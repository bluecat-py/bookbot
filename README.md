# Bookbot

Bookbot is a command-line application built with Python that analyzes text files and generates statistics about the words and characters contained within them.

## Features

- Counts the total number of words in a text
- Counts the frequency of each character
- Sorts character frequencies by occurrence
- Displays the analysis in a readable report format

## Technologies Used

- Python

## What I Learned

Through this project, I learned about:

- Functions
- Dictionaries
- File handling
- Data sorting
- Building command-line applications

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/bluecat-py/bookbot.git
```

2. Navigate to the project directory:

```bash
cd bookbot
```

3. Run the program:

```bash
python3 main.py books/frankenstein.txt
```

## Example Output

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
...
============= END ===============
```

