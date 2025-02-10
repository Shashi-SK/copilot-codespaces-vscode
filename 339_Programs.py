#3
import pandas as pd
# Assuming you have loaded the dataset into a DataFrame called 'df'
# (replace 'robot_dataset(robot_dataset)_1.csv' with the actual file name)
df = pd.read_csv('robot_dataset(robot_dataset)_1.csv')
# 1) Average number of conversations
avg_conversations = df['Interaction_Count'].mean()
print(f"Average daily conversations: {avg_conversations}")
# 2) Total steps walked (assuming you want the sum for the entire dataset)
total_steps = df['Steps_Walked'].sum()
print(f"Total steps walked: {total_steps}")
# 3) Maximum and minimum energy consumption
max_energy = df['Energy_Consumption (kWh)'].max()
min_energy = df['Energy_Consumption (kWh)'].min()
print(f"Maximum energy consumption: {max_energy}")
print(f"Minimum energy consumption: {min_energy}")
# 4) Correlation between steps walked and energy consumption
correlation = df['Steps_Walked'].corr(df['Energy_Consumption (kWh)'])
print(f"Correlation between steps and energy: {correlation}")
# 5) Distribution of objects recognized (using a histogram)
import matplotlib.pyplot as plt  # Import matplotlib for plotting
plt.hist(df['Objects_Recognized'])
plt.xlabel('Objects Recognized')
plt.ylabel('Frequency')
plt.title('Distribution of Objects Recognized')
plt.show()
# 6) Variance in learning sessions
variance_learning = df['Learning_Sessions'].var()
print(f"Variance in learning sessions: {variance_learning}"

# 4 Declare variables of different data types
name = "Alice"  # String
age = 30      # Integer
height = 5.8   # Float
is_student = False  # Boolean
# Output the variables in a sentence format using f-strings
print(f"My name is {name}, I am {age} years old, I am {height} feet tall, and it is {is_student} that I am a student.")
# More examples of different sentence structures:
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Is a student: {is_student}")
# You can also do calculations directly within the f-string:
next_year_age = age + 1
print(f"Next year, I will be {next_year_age} years old.")
# And you can use different formatting options:
pi = 3.14159265359
print(f"Pi rounded to two decimal places: {pi:.2f}") # Output: 3.14
# Boolean values are automatically formatted as "True" or "False":
print(f"Am I a student? {is_student}") # Output: Am I a student? False

# 5. Check if a number is positive, negative, or zero

num = int(input("Enter an integer: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# 6. Print multiplication table

num = int(input("Enter a number for the multiplication table: "))

print(f"Multiplication Table for {num}:")
for i in range(1, 11):  # Loop from 1 to 10 (inclusive)
    print(f"{num} x {i} = {num * i}")


#7.Create a Python list that contains the names of 5 different fruits. Perform the given operations on the list.
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
fruits.append("Fig")
fruits.remove("Banana")
print("Updated list:", fruits)


# 8 Create a tuple with 5 numbers
my_tuple = (10, 20, 30, 40, 50)
# Print the tuple
print("Original tuple:", my_tuple)
# Access elements (indexing)
print("Element at index 2:", my_tuple[2])  # Output: 30
# Slicing
print("Elements from index 1 to 3:", my_tuple[1:4])  # Output: (20, 30, 40)
# Concatenation
another_tuple = (60, 70)
combined_tuple = my_tuple + another_tuple
print("Combined tuple:", combined_tuple)
# Length of the tuple
print("Length of the tuple:", len(my_tuple))
# Check if an element exists
print("Is 30 in the tuple?", 30 in my_tuple)  # Output: True
print("Is 80 in the tuple?", 80 in my_tuple)  # Output: False
# Count occurrences of an element
print("Number of times 20 appears:", my_tuple.count(20)) # Output: 1
# Tuple packing and unpacking
a, b, c, d, e = my_tuple  # Unpacking
print("Unpacked values:", a, b, c, d, e)
# To "modify" a tuple, you need to create a new one:
modified_tuple = (100,) + my_tuple[1:] # Creates a new tuple with the first element changed.
print("Modified tuple:", modified_tuple)
# Iterating through the tuple
print("Iterating through the tuple:")
for item in my_tuple:
    print(item)


#9.Create a dictionary that stores the names of 3 students as keys and their marks in mathematics as
#values. Perform the given operations.
tuple_numbers = (10, 20, 30, 40, 50)
print("Tuple length:", len(tuple_numbers))
print("Tuple sum:", sum(tuple_numbers))

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
print("Bob's Marks:", students["Bob"])
students["David"] = 88
del students["Alice"]
print("Updated dictionary:", students)


#10.Create two sets of integers. Perform the given set operations.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)


#11. Function to find the largest number in a list
def find_largest(numbers):
    if not numbers:  
        return None  
    largest = numbers[0]  
    for number in numbers:
        if number > largest:
            largest = number
    return largest
numbers = [10, 5, 20, 8, 15]
largest_number = find_largest(numbers)
print(f"The largest number in the list is: {largest_number}")  
numbers_empty = []
largest_number_empty = find_largest(numbers_empty)
print(f"The largest number in the empty list is: {largest_number_empty}")


#12. List comprehension for squares of even numbers
even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(f"Squares of even numbers between 1 and 20: {even_squares}")


#14. NumPy array creation and information
import numpy as np

# One-dimensional array
arr1d = np.array([1, 2, 3, 4, 5])
print("One-dimensional array:")
print(arr1d)
print("Shape:", arr1d.shape)
print("Dimensions:", arr1d.ndim)

# Two-dimensional array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\nTwo-dimensional array:")
print(arr2d)
print("Shape:", arr2d.shape)
print("Dimensions:", arr2d.ndim)

# Three-dimensional array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\nThree-dimensional array:")
print(arr3d)
print("Shape:", arr3d.shape)
print("Dimensions:", arr3d.ndim)

#15. Write a Python program to create a 5x5 NumPy array of random integers and Perform array indexing as given.
import numpy as np
random_array = np.random.randint(1, 100, (5, 5))
print("Random 5x5 array:", random_array)
print("Element at (2,3):", random_array[2, 3])


#16.create a NumPy array of shape (4, 4) containing numbers from 1 to 16. Use slicing to extract for the given conditions
import numpy as np
matrix = np.arange(1, 17).reshape(4, 4)
print("First row:", matrix[0, :])
print("Last column:", matrix[:, -1])
print("Sub-matrix:", matrix[1:3, 1:3])


#18. Write a Python program to demonstrate broadcasting. Create an array of shape (3, 3) and add a one-
#dimensionalarrayof shape (1, 3) to it using broadcasting.
arrA = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arrB = np.array([10, 20, 30])
print("Broadcasted Sum:", arrA + arrB)


#19. Create two NumPy arrays of the same shape, A and B. Perform the following arithmetic operations:Element-wise addition.Element-wise subtraction.Element-wise multiplication.Element-wise division.
import numpy
A = numpy.array([[1, 2], [3, 4]])
B = numpy.array([[5, 6], [7, 8]])
print("Addition:", A + B)
print("Subtraction:", A - B)
print("Multiplication:", A * B)
print("Division:", A / B)


#20. Create a Pandas DataFrame with the given Name and marks of 3 courses:Add a new column named 'Total' that represents the sum of all the courses. Add 'Grade' based on the values of the 'Total'. Print the updated DataFrame with the new 'Total' and 'Grade'column.
import pandas as pd
data = {"Name": ["Alice", "Bob", "Charlie"], "Math": [85, 90, 78], "Science": [88, 76, 94], "English": [92, 80, 85]}
df = pd.DataFrame(data)
df["Total"] = df.iloc[:, 1:].sum(axis=1)
df["Grade"] = df["Total"].apply(lambda x: "A" if x > 250 else "B")
print(df)










