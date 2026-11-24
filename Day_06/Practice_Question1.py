Employee = (203,"Karan Nair","Sales",72)
print(Employee)
print(type(Employee))
emp_id ,name,department,score = Employee
print(emp_id)
print(name)
print(department)
print(score)
print(Employee[1])
print(Employee[2:])
if score >= 90:
    Grade = "A"
elif score >=80:
    Grade = "B"
elif score >= 70:
    Grade = "C"
elif score >= 60:
    Grade ="D"
else:
    Grade ="Fail"
print("Grade :",Grade)
if score >= 60:
    print("Passed")
else:
    print("Failed")
scores_list =[88,95,72,72,55,64]
print(scores_list)
print(min(scores_list))
print(max(scores_list))
print(sum(scores_list))
print(scores_list.count(72))
scores_list.append(70)
print(len(scores_list))
scores_list.sort()
print(scores_list)
department_list = ["Sales","HR","Sales","Finance","HR","Finance"]
department_list = set(department_list)
print(department_list)
print(len(department_list))
print(department in department_list)
Alpha = {"Rohan Pillai","Priya Shetty","Karan Nair"}
Beta = {"Divya Rao","Karan Nair","Manoj Das"}
print(Alpha & Beta)
print(Alpha | Beta)
print(Alpha - Beta)
Alpha.add("Divya Rao")
print(Alpha)
Alpha.remove("Karan Nair")
print(Alpha)
print("Emo id: ",emp_id)
print("Name :",name)
print("Department :",department)
print("Score : ",score)
print("Grade : ",Grade)
if score >= 60:
    print("Pass")
else:
    print("Fail")
if name in Alpha:
    print("In Alpha Team: Yes")
else:
    print("In Alpha Team: No")