# File Handling Demo

# Write data to a file
with open("student.txt", "w") as file:
    file.write("Name : Manasa\n")
    file.write("Department : AI & DS\n")
    file.write("CGPA : 8.2\n")

print("Data written successfully!")

# Read data from the file
with open("student.txt", "r") as file:
    data = file.read()

print("\nStudent Details")
print(data)

# Append new data
with open("student.txt", "a") as file:
    file.write("College : Dhanalakshmi Srinivasan Engineering College\n")

print("New data appended successfully!")

# Display updated file
with open("student.txt", "r") as file:
    print("\nUpdated File Content")
    print(file.read())
