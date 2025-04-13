import json
from datetime import datetime, timedelta

class Book:
    def __init__(self, isbn, title, author, quantity):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.isbn}: {self.title} by {self.author} (Available: {self.quantity})"
    
    def to_dict(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'quantity': self.quantity
        }

class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []
    
    def __str__(self):
        return f"Member ID: {self.member_id}\nName: {self.name}\nEmail: {self.email}"
    
    def to_dict(self):
        return {
            'member_id': self.member_id,
            'name': self.name,
            'email': self.email,
            'borrowed_books': self.borrowed_books
        }

class Transaction:
    def __init__(self, book_isbn, member_id, issue_date, return_date=None):
        self.book_isbn = book_isbn
        self.member_id = member_id
        self.issue_date = issue_date
        self.return_date = return_date
    
    def to_dict(self):
        return {
            'book_isbn': self.book_isbn,
            'member_id': self.member_id,
            'issue_date': self.issue_date.strftime('%Y-%m-%d'),
            'return_date': self.return_date.strftime('%Y-%m-%d') if self.return_date else None
        }

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.transactions = []
        self.load_data()
    
    def add_book(self, book):
        if book.isbn in self.books:
            self.books[book.isbn].quantity += book.quantity
        else:
            self.books[book.isbn] = book
    
    def register_member(self, member):
        if member.member_id in self.members:
            raise ValueError("Member ID already exists")
        self.members[member.member_id] = member
    
    def issue_book(self, isbn, member_id, days=14):
        if isbn not in self.books:
            raise ValueError("Book not found")
        if member_id not in self.members:
            raise ValueError("Member not registered")
        if self.books[isbn].quantity <= 0:
            raise ValueError("Book not available")
        
        issue_date = datetime.now()
        return_date = issue_date + timedelta(days=days)
        
        self.books[isbn].quantity -= 1
        self.members[member_id].borrowed_books.append(isbn)
        transaction = Transaction(isbn, member_id, issue_date, return_date)
        self.transactions.append(transaction)
        return transaction
    
    def return_book(self, isbn, member_id):
        if isbn not in self.books:
            raise ValueError("Book not found")
        if member_id not in self.members:
            raise ValueError("Member not registered")
        if isbn not in self.members[member_id].borrowed_books:
            raise ValueError("This member hasn't borrowed this book")
        
        self.books[isbn].quantity += 1
        self.members[member_id].borrowed_books.remove(isbn)
        
        # Update the transaction record
        for transaction in self.transactions:
            if (transaction.book_isbn == isbn and 
                transaction.member_id == member_id and 
                transaction.return_date is None):
                transaction.return_date = datetime.now()
                break
    
    def search_book(self, **kwargs):
        results = []
        for book in self.books.values():
            match = True
            for key, value in kwargs.items():
                if str(getattr(book, key)).lower() != str(value).lower():
                    match = False
                    break
            if match:
                results.append(book)
        return results
    
    def save_data(self):
        data = {
            'books': [book.to_dict() for book in self.books.values()],
            'members': [member.to_dict() for member in self.members.values()],
            'transactions': [t.to_dict() for t in self.transactions]
        }
        
        try:
            with open('library_data.json', 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def load_data(self):
        try:
            with open('library_data.json', 'r') as f:
                data = json.load(f)
                
                for book_data in data.get('books', []):
                    book = Book(
                        book_data['isbn'],
                        book_data['title'],
                        book_data['author'],
                        book_data['quantity']
                    )
                    self.books[book.isbn] = book
                
                for member_data in data.get('members', []):
                    member = Member(
                        member_data['member_id'],
                        member_data['name'],
                        member_data['email']
                    )
                    member.borrowed_books = member_data.get('borrowed_books', [])
                    self.members[member.member_id] = member
                
                for trans_data in data.get('transactions', []):
                    transaction = Transaction(
                        trans_data['book_isbn'],
                        trans_data['member_id'],
                        datetime.strptime(trans_data['issue_date'], '%Y-%m-%d'),
                        datetime.strptime(trans_data['return_date'], '%Y-%m-%d') if trans_data['return_date'] else None
                    )
                    self.transactions.append(transaction)
                    
        except FileNotFoundError:
            print("No existing data found. Starting with empty library.")
        except json.JSONDecodeError:
            print("Error reading data file. Starting with empty library.")
        except Exception as e:
            print(f"Error loading data: {e}. Starting with empty library.")

def display_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Display All Books")
    print("7. Display All Members")
    print("8. Exit")

def main():
    library = Library()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")
        
        try:
            if choice == '1':
                isbn = input("Enter ISBN: ")
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                quantity = int(input("Enter Quantity: "))
                book = Book(isbn, title, author, quantity)
                library.add_book(book)
                print("Book added successfully!")
            
            elif choice == '2':
                member_id = input("Enter Member ID: ")
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                member = Member(member_id, name, email)
                library.register_member(member)
                print("Member registered successfully!")
            
            elif choice == '3':
                isbn = input("Enter Book ISBN: ")
                member_id = input("Enter Member ID: ")
                days = int(input("Enter number of days to borrow (default 14): ") or 14)
                transaction = library.issue_book(isbn, member_id, days)
                print(f"Book issued successfully! Due date: {transaction.return_date.strftime('%Y-%m-%d')}")
            
            elif choice == '4':
                isbn = input("Enter Book ISBN: ")
                member_id = input("Enter Member ID: ")
                library.return_book(isbn, member_id)
                print("Book returned successfully!")
            
            elif choice == '5':
                print("Search by:")
                print("1. ISBN")
                print("2. Title")
                print("3. Author")
                search_choice = input("Enter search option (1-3): ")
                
                if search_choice == '1':
                    isbn = input("Enter ISBN: ")
                    results = library.search_book(isbn=isbn)
                elif search_choice == '2':
                    title = input("Enter Title: ")
                    results = library.search_book(title=title)
                elif search_choice == '3':
                    author = input("Enter Author: ")
                    results = library.search_book(author=author)
                else:
                    print("Invalid choice")
                    continue
                
                if results:
                    print("\nSearch Results:")
                    for book in results:
                        print(book)
                else:
                    print("No books found matching your criteria.")
            
            elif choice == '6':
                if library.books:
                    print("\nAll Books:")
                    for book in library.books.values():
                        print(book)
                else:
                    print("No books in the library.")
            
            elif choice == '7':
                if library.members:
                    print("\nAll Members:")
                    for member in library.members.values():
                        print(member)
                        if member.borrowed_books:
                            print("Borrowed Books:", ", ".join(member.borrowed_books))
                        print()
                else:
                    print("No members registered.")
            
            elif choice == '8':
                library.save_data()
                print("Data saved. Exiting...")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1-8.")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()