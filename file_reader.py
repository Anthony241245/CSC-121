# Read data from a text file
# Open the file in read mode
name_list = []
grade_list = []
with open("student_scores.txt", "r") as file:
    print(file)
    for line in file:
        print(line.strip())  # strip() removes extra whitespace and newline characters
        name, grade = line.split(", ")
        name_list.append(name)
        grade_list.append(int(grade.strip()))


print(name_list)
print()
print(grade_list)
print()
print()
print(f"The average grade for student is: {sum(grade_list)/len(grade_list)} ")
file.close()

with open("student_scores.txt", "a") as file: # Use "a" mode to appead
    file.write(f"\nThe average grade for student is: {sum(grade_list)/len(grade_list)} ")  




