# Example 1: Bank Account Management
# Scenario: Create a BankAccount class to manage bank accounts with functionalities like deposit, withdrawal, and displaying balance.

class BankAccount:
    account_number_counter = 1000
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        self.account_number = BankAccount.account_number_counter
        BankAccount.account_number_counter += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit: {amount}, New Balance is: {self.balance}.")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw: {amount}, New Balance is: {self.balance}.")
        elif amount > self.balance:
            print("Insufficient Balance.")
        else:
            print("Deposit must be positive.")
    def display_balance(self):
        print(f"Account {self.account_number} owned by: {self.owner} has balance: ${self.balance}")

acc1 = BankAccount("Alice", 500)
acc1.display_balance()
acc1.deposit(3000)
acc1.withdraw(3000)

print()
acc2 = BankAccount("Abdullah", 4000)
acc2.deposit(433)
acc2.display_balance()


print()

# Example 2: Library Management System
# Scenario: Create classes to manage books and library members, allowing members to borrow and return books.

class Book:

    def __init__(self, title, author, no_of_book=1):
        self.title = title
        self.author = author
        self.no_of_book = no_of_book

    def borrow(self):
        if self.no_of_book > 0:
            self.no_of_book -= 1
            print(f"Book '{self.title}' has been borrowed.")
            return True
        else:
            print(f"There is no available  Item to Book '{self.title}'. Please Try After few days.")
            return False
    def return_book(self):
        self.no_of_book += 1
        print(f"Book '{self.title}' has been returned.")

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_book = []

    def borrow_book(self, book):
        if book.title not in self.borrowed_book and book.borrow():
            self.borrowed_book.append(book.title)
            print(f"{self.name} borrowed '{book.title}'.")
        elif book.title in self.borrowed_book:
            print(f"{self.name} cannot borrow '{book.title}' as it is already borrowed.")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")

    def return_book(self, book):
        if book.title in self.borrowed_book:
            book.return_book()
            self.borrowed_book.remove(book.title)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")

book1 = Book("1984", "George Orwell",2)
book2 = Book("To Kill a Mockingbird", "Harper Lee")

member1 = Member("Alice")
member2 = Member("Bob")
member3 = Member("Abdullah")

member1.borrow_book(book1)
print()

member2.borrow_book(book1)
print()

member3.borrow_book(book1)
print()

member2.return_book(book1)
print()

member3.borrow_book(book1)
print()

member2.borrow_book(book2)


print()

# Example 3: Employee Management with Inheritance
# Scenario: Create a base Employee class and derived classes like Developer and Manager, each with specific attributes and methods.
#

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name}  is working")

    def __str__(self):
        return  f"Employee(Name: {self.name}, Salary: {self.salary})"

class Developer(Employee):
    def __init__(self, name, salary, p_lang):
        super().__init__(name, salary)
        self.p_lang = p_lang

    def work(self):
        return f"{self.name} is coding in {self.p_lang}."

    def __str__(self):
        return f"Developer(Name: {self.name}, Salary: ${self.salary}, Language: {self.p_lang})"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        return f"{self.name} is coding in {self.team_size}."

    def __str__(self):
        return f"Developer(Name: {self.name}, Salary: ${self.salary}, Language: {self.team_size})"


em = Employee("Abu Huraira", 400000)
pr = Developer("Abdur Rahman", 500000, "C++, Java, Python, JavaScript, C, PHP(Basics)")
mgr = Manager("Abdullah", 7000000, 10)

print(em)
print(pr)
print(mgr)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} is working."

    def __str__(self):
        return f"Employee(Name: {self.name}, Salary: ${self.salary})"


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def work(self):
        return f"{self.name} is coding in {self.programming_language}."

    def __str__(self):
        return f"Developer(Name: {self.name}, Salary: ${self.salary}, Language: {self.programming_language})"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        return f"{self.name} is managing a team of {self.team_size} people."

    def __str__(self):
        return f"Manager(Name: {self.name}, Salary: ${self.salary}, Team Size: {self.team_size})"


# Usage
emp = Employee("Charlie", 50000)
dev = Developer("Dana", 80000, "Python")
mgr = Manager("Eve", 90000, 10)

print(emp)  # Output: Employee(Name: Charlie, Salary: $50000)
print(dev)  # Output: Developer(Name: Dana, Salary: $80000, Language: Python)
print(mgr)  # Output: Manager(Name: Eve, Salary: $90000, Team Size: 10)

print(emp.work())  # Output: Charlie is working.
print(dev.work())  # Output: Dana is coding in Python.
print(mgr.work())  # Output: Eve is managing a team of 10 people.
