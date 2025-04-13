import csv

class Employee:
    def __init__(self, empid, name, address, contact_number, spouse_name, number_of_child, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_child = number_of_child
        self.salary = salary
    
    def __str__(self):
        return (f"ID: {self.empid}\nName: {self.name}\nAddress: {self.address}\n"
                f"Contact: {self.contact_number}\nSpouse: {self.spouse_name}\n"
                f"Children: {self.number_of_child}\nSalary: {self.salary}\n")

def input_employee():
    try:
        empid = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        address = input("Enter Address: ")
        contact_number = input("Enter Contact Number: ")
        spouse_name = input("Enter Spouse Name: ")
        number_of_child = int(input("Enter Number of Children: "))
        salary = float(input("Enter Salary: "))
        return Employee(empid, name, address, contact_number, spouse_name, number_of_child, salary)
    except ValueError as e:
        print(f"Error in input: {e}. Please enter valid data.")
        return None

def save_to_csv(employees, filename="employees.csv"):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Employee ID", "Name", "Address", "Contact Number", 
                            "Spouse Name", "Number of Children", "Salary"])
            for emp in employees:
                writer.writerow([emp.empid, emp.name, emp.address, emp.contact_number,
                               emp.spouse_name, emp.number_of_child, emp.salary])
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

def display_employees(filename="employees.csv"):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            print("\nEmployee List:")
            print("-" * 50)
            for i, row in enumerate(reader):
                if i == 0:  # Skip header
                    print(f"{row[0]:<12} {row[1]:<20} {row[2]:<15} {row[3]:<15} {row[6]:>10}")
                    print("-" * 50)
                    continue
                print(f"{row[0]:<12} {row[1]:<20} {row[2]:<15} {row[3]:<15} ${float(row[6]):>9,.2f}")
    except FileNotFoundError:
        print("No employee data found. Please add employees first.")
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    employees = []
    
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Save and Exit")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
            
            if choice == 1:
                emp = input_employee()
                if emp:
                    employees.append(emp)
            elif choice == 2:
                if employees:
                    print("\nCurrent Employees:")
                    for emp in employees:
                        print(emp)
                else:
                    # Try to read from file if no in-memory data
                    display_employees()
            elif choice == 3:
                if employees:
                    save_to_csv(employees)
                else:
                    print("No employee data to save.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number (1-3).")

if __name__ == "__main__":
    main()