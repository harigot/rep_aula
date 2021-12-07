'''
4. Add a class variable named domains to the following Employee class. Make this class variable a 
set and it should store all domain names used by employees.

class Employee:    
    def __init__(self,name,email):
        self.name = name
        self.email = email
   
   def display(self):
        print(self.name, self.email)
            
e1 = Employee('John','john@gmail.com')
e2 = Employee('Jack','jack@yahoo.com')
e3 = Employee('Jill','jill@outlook.com')
e4 = Employee('Ted','ted@yahoo.com')
e5 = Employee('Tim','tim@gmail.com')
e6 = Employee('Mike','mike@yahoo.com')


5. In the following Employee class, add a class variable named allowed_domains.
allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}
Whenever an email is assigned, if the domain named is not in allowed_domains, raise a RuntimeError.

class Employee:
 
    def __init__(self,name,email):
        self.name = name
        self.email = email
 
    def display(self):
        print(self.name, self.email)
 
e1 = Employee('John','john@gmail.com')
e2 = Employee('Jack','jack@yahoo.com')
e3 = Employee('Jill','jill@outlook.com')
e4 = Employee('Ted','ted@yahoo.com')
e5 = Employee('Tim','tim@xmail.com')
'''



class Employee:
    domains = []
    alowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}
    
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.validate_email()
        Employee.domains.append(self.name)
        Employee.domains.append(self.email.split('@')[-1])
   
    def validate_email(self):
        assert self.email.split('@')[-1] in Employee.alowed_domains, 'Invalid domain'

    def __str__(self):
        return f'name: {self.name}, email:{self.email}'
            

e1 = Employee('John','john@gmail.com')
e2 = Employee('Jack','jack@yahoo.com')
e3 = Employee('Jill','jill@outlook.com')
e4 = Employee('Ted','ted@yahoo.com')
e5 = Employee('Tim','tim@gmail.com')
e6 = Employee('Mike','mike@yahoo.com')
print(Employee.domains)
