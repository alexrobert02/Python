import os
import sys


def count_files_by_extension(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        if not os.listdir(directory):
            print(f"The directory '{directory}' is empty.")
            return

        extension_counts = {}

        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            try:
                if os.path.isfile(file_path):
                    _, extension = os.path.splitext(filename)

                    extension_counts[extension] = extension_counts.get(extension, 0) + 1
            except Exception as e:
                print(f"Error accessing file '{file_path}': {e}")

        if extension_counts:
            print("File counts by extension:")
            for ext, count in extension_counts.items():
                print(f"{ext}: {count} files")
        else:
            print(f"No valid files found in the directory '{directory}'.")

    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    count_files_by_extension(directory_path)


if __name__ == "__main__":
    main()
