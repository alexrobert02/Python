#   Write a function that counts how many words exists in a text. A text is considered to be form out of words that are
# separated by only ONE space. For example: "I have Python exam" has 4 words.


def count_words(text):
    words = text.split()
    num_words = len(words)

    return num_words


def main():
    text = "I have Python exam"

    print(f'"{text}" has {count_words(text)} words.')


if __name__ == "__main__":
    main()
