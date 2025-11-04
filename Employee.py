# Program #4 EmployeeDatabase, Griffin Corneia, 11/3/25:

class Employee:

    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def display_info(self):
        print(self.name)
        print(self.id_number)
        print(self.department)
        print(self.job_title)
        print("")

def main():
    print("Employee Information")
    print("")

    employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

    employee1.display_info()
    employee2.display_info()
    employee3.display_info()

if __name__ == "__main__":
    main()