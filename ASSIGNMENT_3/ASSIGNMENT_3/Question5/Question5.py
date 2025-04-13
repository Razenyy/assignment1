def count_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()  
            words = text.split()  

            word_count = {}
            for word in words:
                
                word = ''.join(char for char in word if char.isalnum())

                if word:
                    word_count[word] = word_count.get(word, 0) + 1

            
            print("\nWord Count:")
            for word, count in sorted(word_count.items()):
                print(f"{word}: {count}")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

count_words('sample.txt')
