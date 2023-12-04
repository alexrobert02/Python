import os
import sys


def calculate_total_size(directory):
    total_size = 0

    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)

                try:
                    file_size = os.path.getsize(file_path)
                    total_size += file_size
                except Exception as e:
                    print(f"Error accessing file '{file_path}': {e}")

        print(f"Total size of all files in '{directory}': {total_size} bytes")

    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    calculate_total_size(directory_path)


if __name__ == "__main__":
    main()
