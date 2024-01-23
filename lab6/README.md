# Lab 6

1. Create a Python script that does the following:
   * Takes a directory path and a file extension as command line arguments (use sys.argv).
   * Searches for all files with the given extension in the specified directory (use os module).
   * For each file found, read its contents and print them.
   * Implement exception handling for invalid directory paths, incorrect file extensions, and file access errors.


2. Write a script using the os module that renames all files in a specified directory to have a sequential number prefix. For example, file1.txt, file2.txt, etc. Include error handling for cases like the directory not existing or files that can't be renamed.


3. Create a Python script that calculates the total size of all files in a directory provided as a command line argument. The script should:
   * Use the sys module to read the directory path from the command line.
   * Utilize the os module to iterate through all the files in the given directory and its subdirectories.
   * Sum up the sizes of all files and display the total size in bytes.
   * Implement exception handling for cases like the directory not existing, permission errors, or other file access issues.


4. Write a Python script that counts the number of files with each extension in a given directory. The script should:
   * Accept a directory path as a command line argument (using sys.argv).
   * Use the os module to list all files in the directory.
   * Count the number of files for each extension (e.g., .txt, .py, .jpg) and print out the counts.
   * Include error handling for scenarios such as the directory not being found, no read permissions, or the directory being empty.