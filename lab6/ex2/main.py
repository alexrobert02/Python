import os
import sys


def rename_files_with_sequence(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        files = [f for f in os.listdir(directory) if f.endswith('.txt') and os.path.isfile(os.path.join(directory, f))]

        for index, filename in enumerate(files, start=1):
            old_path = os.path.join(directory, filename)
            new_filename = f"file{index}.{filename.split('.')[-1]}"
            new_path = os.path.join(directory, new_filename)

            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")
            except Exception as e:
                print(f"Error renaming file '{filename}': {e}")

    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    rename_files_with_sequence(directory_path)


if __name__ == "__main__":
    main()
