'''
Program to copy the contents of one file to another.
'''

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()

        with open(destination_file, 'w') as dest:
            dest.write(content)

        print(f"Contents successfully copied from '{source_file}' to '{destination_file}'.")

    except FileNotFoundError:
        print("Error: The source file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


source = input("Enter the source file name (e.g., file1.txt): ")
destination = input("Enter the destination file name (e.g., file2.txt): ")
copy_file(source, destination)
