import os
print(f"Current working directory: {os.getcwd()}")


import csv

def display_csv(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            # Read and display headers
            headers = next(reader, None)  # Read the header row
            if headers:
                print(f"{' | '.join(headers)}")  # Print headers in a nice format
                print('-' * 50)  # Separator line

            # Read and display the rows
            for row in reader:
                print(f"{' | '.join(row)}")
    except FileNotFoundError:
        print("Error: The CSV file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to display the CSV file
display_csv('/Users/suraj/Desktop/Python/Question4/data.csv')
