# DATA TYPES 
# int 
-88
23
# float
# print(23.545)
# str
'damm'
"dog"

# bool
True
False

# print("hello world", 454, True )
# print("hello world", 454, True, end="|")  


# # setting value
# hello = "gerald"
# world = "world"
# print("it is " + hello , world)
# hello_world #snake case
# helloWorld #camel case

# 312k = "wewe" # wont work
# print(312)

# name = input("Name: ")
# age  = input('Age: ')
# print("I am "+  name + " am ", age + " years old")
# print("I am", name, "am", age , "years old")

# x = 9
# y = 3.5
# result = int(x * y) # +- / // %
# BEDMAS exponential 
# print(result)
# num = input('Number: ')
# print(num-5)  # wont work because automatically num is a string
# print(float(num) -5)


#string method
hello =  'hello'.capitalize()
world = "world".upper()
# print(type(hello))
# print(hello, world)
# print(world.count('R'))

# x = 'hello '
# y = 2
# z = "world"
# print(x*y)
# print(x + z)

# CONDITION OPERATORS
# == != <= >= < > 

# X = "hello"
# Y = "HELLO"
# print(x == y)
# print('ab' > 'djjj')
# print(ord('D'))


# CHAINED CONDTIONAL
#and or not
# x = 6
# y = 8
# z = 0
# result1 = x == y
# result2 = y < x
# result3 = z < x + 2
# result4  = result1 or  result2 or result3
# print(result4)


# print(not True)

# if x == 7:
#     print(True)
# elif x > 7:
#     print('x is not greater  than 7')
# else:
#     print ('x is less than 7')

# x =[4,5,3,True, "kask"]  #list
# y=("rew","sss",) #tuple it cant be changed when defined
# print(x)
# print(len(y))
# x.append('world')  # you can append to list not tuple
# x.extend([12,3,212,43])
# # x.pop() # will remove the last element
# # x.pop(2)  #remove index 2
# x[3] = "damm" # tuple is a no no 
# print(x)


# for i in range(10):
#     print(i)
    
# start, stop, step
# for i in range(10, -1,-1):
#     print(i)

# for i in [1,2,3569,4,3,342,1,1,12376,756,7655]:
#     print(i)

# x=[1,2,3569,4,3,342,76551,1,12376,756,342,76551,1,12376,756]
# for i in range(len(x)):
    # print(x[i])
    # print(i) # it will just go for the index

# for i , element in enumerate(x):
#     print(i, element)

# for i in x:
#     print(i)

# i = 0
# while i < 10:
#     print('run')
#     i += 1
#     if i == 3:
#         break


#SLICED OPERATOR

# sliced = [start:stop:step]
# x = [0,1,2,3,4,5,6,7,8,9,10]
# sliced = x[0:8:2]
# step  = x[::2]
# print(step)


#SET
# x = set()
# s= {4,5,23,34,34}
# s2 = {76,98,23,9,56,56,5,56}
# s.add(45)
# # s.remove(23)

# print(s)
# print(76 in s2)
# print(s.union(s2))
# print(s.difference(s2))
# print(s.intersection(s2))


# x = {'key': 4}
# x['key2'] = 5
# x[20]  = [2,43,554]
# # del x[20]
# for key, value in x.items():
#     print(key, value)
# print(x)


#COMPREHENSION
x= [x+ 6  for x in range(5)]
print(x)


