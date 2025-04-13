# Program to count the number of lines, words, and characters in a text file.
def count_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            line_count = len(lines)
            word_count = 0
            char_count = 0

            for line in lines:
                words = line.split()
                word_count += len(words)
                char_count += len(line)

            print(f"File: {filename}")
            print(f"Total Lines: {line_count}")
            print(f"Total Words: {word_count}")
            print(f"Total Characters: {char_count}")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")


filename = input("Enter the name of the text file (with .txt extension): ")
count_file_contents(filename)
