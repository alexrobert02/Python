import os
import sys


def read_and_print_files(directory, extension):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        if not extension.startswith("."):
            raise ValueError("File extension should start with a dot (e.g., '.txt').")

        for filename in os.listdir(directory):
            _, ext = os.path.splitext(filename)
            if ext == extension:
                file_path = os.path.join(directory, filename)

                try:
                    with open(file_path, 'r') as file:
                        content = file.read()
                        print(f"Contents of '{filename}':\n{content}\n")
                except Exception as e:
                    print(f"Error reading file '{filename}': {e}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
        sys.exit(1)

    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    read_and_print_files(directory_path, file_extension)


if __name__ == "__main__":
    main()
