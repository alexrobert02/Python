def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words


def main():
    text = "I have Python exam"
    print(f'"{text}" has {count_words(text)} words.')


if __name__ == "__main__":
    main()
