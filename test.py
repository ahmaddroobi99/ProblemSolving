# Design database schema for the following entities:
# Company, Department, Employee and Task
# Note: a Task can involve more than one employee, for example a task can have two
# employees one with "worker" role and the other with "manager" role
#
# Create table Company ;
# Create table Department;
# Create table Employee;
# Create table Task;
#
# comapny (id ,Name , Seriel NBumber)
#
# Department (id, name ,CompanyID)
#
# Employee (id, name,phone ,CompanyID,departmentID,  )
#
# Task (id ,name ,EmpID,countEmp)
#
# Select  * From Employee where company.id ==Department.CompanyID and emmployee.departmentID == Department.id ;





#
# arr= [1,2,3,6,8,7,8,2,4]
# min1 = float("inf")
# min2 =float("inf")
#
# for a in arr :
#     min2 = min1
#     if a<min1 :
#         min1=a
# print(min1)

arr= [1,2,3,6,8,7,8,2,4]
total = 16
# map ={}
# for ele in arr :
#     map[key] =total- ele
# ans =[]
# for ele in arr :
#     sum=total-ele
#     ans.append(ele)
#     if sum==0 :
#         break
# print(ans)





















