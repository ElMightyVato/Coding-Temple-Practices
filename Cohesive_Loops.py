"""
Exercise 1:

1. Create a list of studen names.
2. Use slicing to select the top three students.
3. use a for loop to iterate through the sliced list
4. Print each name with a congratulatory message."""

# students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# top_student = students [:3] #Here we are deciding to only select the first three students in our list

# for student in top_student: # Here we begin our loop by going through our students list one by one by utilitzing student
#     print(f"Congratulations, {student}! You are among the top performers!")

"""
Exercise 2:
1.Loop through the inventory list using a hwile loop and index numbers
2. Use if statem,ents to check the data type of each item
3. Print a message for each item, depending on its data type."""

inventory = ['apples', 120, 'oranges', 80, True, 'bananas', 150, False] #We are assigning boliions to indicate when an item is on sale

index = 0 

while index < len(inventory): # we are looping through the list to loop through our index
    item = inventory[index]

    if type(item) == str: #
        print(f"Item: {item}")
    elif type(item) == int:
        print(f"Quantity: {item}")
    elif type(item) == bool:
        status = "on sale" if item else "not on sale"
        print(f"Sale status: {status}")

    index += 1