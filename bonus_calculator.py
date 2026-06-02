# WAP of an employ for his details like employ_id ,name , department , salary and experience (codnitons : if experience > 5 bonus = 2% ,  )

import numpy as np
n = int(input("Enter no. of employs :"))
emp_dtype = np.dtype([ 
    ('emp_id','i4'),
    ('name', 'U20'),
    ('department', 'U20'),
    ('salary','f8'),
    ('exp', 'i4')
])
emp = np.empty(n,dtype=emp_dtype) #this creates an empty array
for i in range(n):
    print(f"\nEnter the details of employes {i+1}:")
    emp[i]['emp_id'] = int(input('Emp_ID :'))
    emp[i]['name'] = input('Name :')
    emp[i]['department'] = input('Department :')
    emp[i]['salary'] = float(input('Salary :'))
    emp[i]['exp'] = int(input('Experience :'))
print("\n -----Employees details and experience-----")
for i in emp:
    print("\nEmployee ID :", i["emp_id"])
    print("\nName :" ,i['name'])
    print("\nDepartment :" ,i['department'])
    print("\nSalary :" ,i['salary'])
    print("\nExperience :" ,i['exp'])
print("\n-----Bonus calculation based upon experience-----")
for i in range(n):
    if emp[i]['exp']>5:
        bonus  = emp[i]['salary']*0.02
        emp[i]['salary'] += bonus
        print(f"{emp[i]['name']} recieve a bonus of {bonus : .2f}")
    else :
        print(f"{emp[i]['name']} does not recieve a bonus.")
for i in emp:
    print(f"{i['name']} - salary after bonus: {i['salary']: .2f}")
tp = np.sum(i["salary"])
print(f"\n Total payment after bonus : {tp: .2f}")