# Q4
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")
print(f"Monday class: {monday_class}")
print(f"Wednesday class: {wednesday_class}")
print(f"Attended both classes: {monday_class & wednesday_class}") #shift 7
print(f"Attended either classes: {monday_class | wednesday_class}") #shift \
print(f"Only monday: {monday_class - wednesday_class}")
print(f"Only One class: {monday_class ^ wednesday_class}") # ^ = caret, shift 6
allStudents = monday_class | wednesday_class
print("Is Monday subset of all students? ", monday_class <= allStudents) #True
