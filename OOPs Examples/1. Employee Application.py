class Employee():
    
    no_of_emps = 0
    raise_amount = 1.04
    
    no_of_mens_at_org = 0
    no_of_womens_at_org = 0
    
    no_of_employees_above_40 = 0
    no_of_employees_below_40 = 0
    
    no_of_female_employees_above_40 = 0
    no_of_female_employees_below_40 = 0
    no_of_male_employees_above_40 = 0
    no_of_male_employees_below_40 = 0
    
    def __init__(self,firstname,lastname,age,gender,salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.salary = salary
        self.gender = gender
        
        Employee.no_of_emps += 1
        
        if(self.gender == 'M'):
            Employee.no_of_mens_at_org += 1
        if(self.gender == 'F'):
            Employee.no_of_womens_at_org += 1
            
        if(self.age < 40):
            Employee.no_of_employees_below_40 += 1
        else:
            Employee.no_of_employees_above_40 += 1
            
        if(self.age < 40 and self.gender == 'F'):
            Employee.no_of_female_employees_below_40 += 1
        if(self.age > 40 and self.gender == 'F'):
            Employee.no_of_female_employees_above_40 += 1
        
        if(self.age < 40 and self.gender == 'M'):
            Employee.no_of_male_employees_below_40 += 1
        if(self.age > 40 and self.gender == 'M'):
            Employee.no_of_male_employees_above_40 += 1
            
    def fullname(self):
        print(self.firstname+self.lastname)
        
    def raise_salary(self):
        self.salary = self.salary * self.raise_amount
        
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
if __name__ == '__main__':
    emp1 = Employee("Rajath","Kumar",25,'M',12000)
    emp2 = Employee('Katrina','Kaif',35,'F',50000)
    emp3 = Employee('Shahrukh','khan',55,'M',30000)
    
    print('Total Employees: ',Employee.no_of_emps)
    print('Total Men Employees: ',Employee.no_of_mens_at_org)
    print('Total Women Employees: ',Employee.no_of_womens_at_org)
    print('Total No. Of Employees above age 40: ',Employee.no_of_employees_above_40)
    print('Total No. Of Employees below age 40: ',Employee.no_of_employees_below_40)
    print('Total No. Of Female Employees above 40: ',Employee.no_of_female_employees_above_40)
    print('Total No. Of Female Employees below 40: ',Employee.no_of_female_employees_below_40)
    print('Total No. Of Male Employees above 40: ', Employee.no_of_male_employees_above_40)
    print('Total No. of Male Employees below 40: ', Employee.no_of_male_employees_below_40)
    
    # To the Normal Employees Increment
    print('Employee1 Salary Before Increment: ',emp1.salary)
    emp1.raise_salary()
    print('Employee1 Salary After Increment: ',emp1.salary)
    
    #To the Special Employees Increment
    #The Attributes of Employee2 before adding instance variable
    print('Attributes of Employee2(Special Employee) before instance variable: ',emp2.__dict__)
    print('Employee2(Special Employee) Salary Before increment: ',emp2.salary)
    #Adding raise_amount Attribute to the Special Employee
    emp2.raise_amount = 1.10
    #The Attributes of Employee2 after adding instance variable
    print('Attributes of Employee2(Special Employee) after instance variable: ',emp2.__dict__)
    #Salary Before Raise
    print('Employee2(Special Employee) Salary Before increment: ',emp2.salary)
    #Applying Raise of Salary to the Second Employee
    emp2.raise_salary()
    #Salary After Raise
    print('Employee2(Special Employee) Salary after increment: ',emp2.salary)
    
    

        