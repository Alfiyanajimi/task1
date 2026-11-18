#Task 1: Create a List
# student=["ammu","anu","anil","Akash","Meera"]
# # print(student)
# # print(student[0])
# # print(student[-1])
# print(len(student))

#Task 2: Add and Remove Elements
# fruits = ["Apple", "Banana", "Orange", "Mango"]
# fruits.append("Grapes")
# print(fruits)
# fruits = ["Apple", "Banana", "Orange", "Mango","grapes"]
# fruits.insert(1,"pineapple")
# print(fruits)
# fruits = ["Apple","Pineapple", "Orange", "Mango","grapes"]
# fruits.pop()
# # fruits.remove("Banana")
# print(fruits)

#Task 3: Update Elements
# marks = [45, 67, 89, 34, 76]
# marks[0] =55
# marks[3] = 64
# print(marks)
# marks =[55, 67, 89, 64, 76]
# print(min(marks))

#Task 4: Sorting and Calculations
# numbers = [45, 12, 89, 23, 67, 5, 34]
# numbers.sort(reverse=True)
# print("Descending:",numbers)
# numbers = [45, 12, 89, 23, 67, 5, 34]
# print(sum(numbers))
# numbers = [45, 12, 89, 23, 67, 5, 34]
# print(sum(numbers)/len(numbers))

#Task 5: Loop Through a List
# student=["ammu","anu","anil","Akash","Meera"]
# for x in student:
#     # print(x)
#     print(student.index(x),x)
# for name in student:
#     if len(name) > 4:
#        print(name)
# student=["ammu","anu","anil","Akash","Meera"]
# print(len(student))

#Task 6: Remove Duplicates
# numbers = [10, 20, 30, 10, 40, 20, 50, 30]
# num=set(numbers)
# # print(num)
# numbers=list(num)
# numbers.sort()
# print(numbers)

#Task 7: Create a Tuple
# languages = ("Python", "Java", "C", "C++", "PHP")
# # print(languages)
# # print(languages[0])
# # print(languages[-1])
# # print(len(languages))
# if "Python" in languages:
#     print("Python is exists in the tuple")
# else:
#     print("Python is not exists in the tuple")

#Task 8: Tuple Operations
# numbers = (10, 20, 30, 40, 50)
# print(numbers[:3])
# print(numbers[-2:])
# print(max(numbers))
# print(min(numbers))
# print(numbers.count(20))

#Task 9: Tuple Conversion
# colors = ("Red", "Blue", "Green")
# color_list = list(colors) # Convert the tuple into a list.
# # print(color_list)
# color_list.append("Yellow")
# # print(color_list)
# color_list.remove("Blue")
# colors=tuple(color_list)
# print(colors)

Task 10: Student Marks Management Create a list containing the marks of 5 students. Your program should:
marks=[25,36,49,55,68]
# print("Total:",sum(marks))
# print("Avg:",sum(marks)/len(marks))
# print("Highest Mark:",max(marks))
# print("Lowest Mark:",min(marks))

count=0
for x in marks:
    if x >= 40:
      count = count + 1
print(count)
 
# marks.sort(reverse=True)
# print("Decscending:",marks)

#Task 11: Shopping Cart
# cart = ["Milk", "Bread", "Eggs"]
# # print(cart)
# cart.append("Candy")
# cart.remove("Bread")
# if "Milk" in cart:
#  print("Milk is available")
# else:
#  print("Milk is not Available")
# # print(cart)

#Task 12: Employee Records Using Tuples Create a tuple for each employee containing Employee ID, Employee Name, Department, and Salary. Create at least 3 employee records. Your program should:
# employees = [
#     (101, "Anu", "HR", 25000),
#     (102, "John", "IT", 35000),
#     (103, "David", "Finance", 40000)
# ]
# # print(employees)
# # for name in employees:
# #       print(name[1])

# print(max(employees))


