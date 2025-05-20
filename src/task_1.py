class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __str__(self):
        return f'{self.first} {self.last} ({self.pay})'

    # print(emp_1)
    #
    # s_emp = str(emp_1)
    #
    # print(type(s_emp))
    # print(s_emp)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.first}, {self.last}, {self.pay})'

    # print(repr(emp_1))

    def __add__(self, other):
        return self.pay + other.pay

    # sum_pay = emp_1 + emp_2
    #
    # print(sum_pay)

    def __len__(self):
        return len(f'{self.first} {self.last}')

emp_1 = Employee('Ivan', 'Ivanov', 50000)
emp_2 = Employee('Petr', 'Petricov', 60000)


print(len(emp_1))
print(len(emp_2))
