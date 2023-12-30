#input_string = input("Enter a list element separated by space ")
#print(input_string)
#list  = input_string.split()
#print("Calculating sum of element of input list")
#sum = 0
#for num in list:
    #sum += int (num)
#print("Sum = ",sum)

# Python program showing how to
# multiple input using split

# taking two inputs at a time
#x, y = input("Enter two values: ").split()
#print("Number of boys: ", x)
#print("Number of girls: ", y)

# taking three inputs at a time
#x, y, z = input("Enter three values: ").split()
#print("Total number of students: ", x)
#print("Number of boys is : ", y)
#print("Number of girls is : ", z)

# taking two inputs at a time
#a, b = input("Enter two values: ").split()
#print("First number is {} and second number is {}".format(a, b))

# taking multiple inputs at a time
# and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
print(x)
# print("List of students: ", x)