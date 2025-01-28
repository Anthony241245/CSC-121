# This program allows the user to calculate tuition cost for students depending on the courses they are taking.
# 1/26/25
# CSC-121 m3Pro - Purchases
# Anhony Raynor

stu_names = ["Zakarri Watson", "Jerom Williams", "Dominique Ross", 'Diana shepard', "Yoko Mayo", "Rashad Ahmed", "Susan Jones"]
courses = ["MAT 035(Concepts of Algebra)", "CTI 115(Computer System Foundations)", "BAS 120 Intro to Analytics", "CSC 121 Python Programming"]
tuition = [460, 520.98, 500, 783.88]



def course_display():
    print(f"{'Course Name':<40} {'Tuition':>10}")
    print("-" * 53)
    for i in range(len(courses)):
        print(f"{courses[i]:<40} ${tuition[i]:>10.2f}")
    
    

def calculate_tuition_all_students():
    Total_tuition = 0
    print(f"{'Stu Name':<20} {'Tuition':>10}")
    print("-" * 30)
    for student in stu_names:
        print(f"Processing tuition for {student}:")
        student_tuition = 0
        for i in range(len(courses)):
            answer = input(f"Is {student} taking {courses[i]}? (Enter 'y' or 'n' ): ")
            if answer == 'y': 
                student_tuition += tuition[i]
        print(f"Total tuition for {student}: ${student_tuition:.2f}")
        print(f"{student:<20} ${student_tuition:>10.2f}")
        total_tuition += student_tuition
    print(f"Total tuition for all students: ${total_tuition:.2f}")
    


def select_student():
    print("Select from the list of student names below:")
    count = 1
    for name in stu_names:
        print(f"{count}) {name}")
        count += 1

    student_number = input("Enter student number: ")
    if student_number.isdigit():
        student_number = int(student_number)
        if 1 <= student_number <= len(stu_names):
            return stu_names[student_number - 1]
        else:
            print("Invalid number. Please select a valid student number.")
    return None


def calculate_tuition_specific_student():
    student_name = select_student()
    print(f"Processing tuition for {student_name}:")
    student_tuition = 0
    print(f"{'Course':<40} {'Tuition':>10}")
    print("-" * 50)
    for i in range(len(courses)):
        answer = input(f"Is {student_name} taking {courses[i]}? (Enter 'y' or 'n' ): ")
        if answer == 'y':  
            student_tuition += tuition[i]
            print(f"{courses[i]:<40} ${tuition[i]:>10.2f}")
    print(f"{'Total Cost':<40} ${student_tuition:>10.2f}")





def main():
    course_display()
    menu_option = 0
    while menu_option != 3:
        print("-------------------- MENU --------------------")
        print("1) Calculate Tuition for ALL Students")
        print("2) Calculate Tuition For Specific Student")
        print("3) Exit")
        print("---------------------------------------------")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            calculate_tuition_all_students()
        elif choice == '2':
            print("Select from list of student names below:")
            for i in range(len(stu_names)):
                print(f"{i + 1}) {stu_names}")
            student_choice = int(input("Enter student number: "))
            if 1 <= student_choice <= len(stu_names):
                calculate_tuition_specific_student(student_choice - 1)
            else:
                print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Exiting program. Goodbye!")
            menu_option = 3
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    

if __name__ == "__main__":
    main()