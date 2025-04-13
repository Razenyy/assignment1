class Student:
    def __init__(self, student_id, name, address, admission_year, level, section):
        self.student_id = student_id
        self.name = name
        self.address = address
        self.admission_year = admission_year
        self.level = level
        self.section = section

    def display_info(self):
        print("\n--- Student Information ---")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Admission Year: {self.admission_year}")
        print(f"Level: {self.level}")
        print(f"Section: {self.section}")



student_id = input("Enter Student ID: ")
name = input("Enter Name: ")
address = input("Enter Address: ")
admission_year = input("Enter Admission Year: ")
level = input("Enter Level (e.g., Undergraduate/Postgraduate): ")
section = input("Enter Section: ")


student = Student(student_id, name, address, admission_year, level, section)


student.display_info()
