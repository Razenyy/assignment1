'''
Program to find and replace a specific word in a file with another word.
'''

def find_and_replace(filename, find_word, replace_word):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        new_content = content.replace(find_word, replace_word)

        
        choice = input("Do you want to overwrite the original file? (yes/no): ").strip().lower()
        if choice == 'yes':
            with open(filename, 'w') as file:
                file.write(new_content)
            print(f"All occurrences of '{find_word}' replaced with '{replace_word}' in the same file.")
        else:
            new_filename = input("Enter the new file name to save the result: ")
            with open(new_filename, 'w') as new_file:
                new_file.write(new_content)
            print(f"All occurrences replaced and saved to '{new_filename}'.")

    except FileNotFoundError:
        print("Error: File not found. Please make sure the file exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


filename = input("Enter the file name (e.g., sample.txt): ")
word_to_find = input("Enter the word to find: ")
word_to_replace = input("Enter the word to replace with: ")
find_and_replace(filename, word_to_find, word_to_replace)
