courses = {
    "MAT-035": {"desc": "Concepts of Algebra", "tuition": 460},
    "CTI-115": {"desc": "Computer System Foundations", "tuition": 520.98},
    "BAS-120": {"desc": "Intro to Analytics", "tuition": 500},
    "CSC-121": {"desc": "Python Programming", "tuition": 783.88}
}
course_codes = courses.keys()

students = {
    "Zakari Watson": ["CTI-115", "CSC-121"],
    "Jerom Williams": ["CTI-115", "CSC-121", "MAT-035", "BAS-120"],
    "Dominique Ross": ["CTI-115", "CSC-121", "MAT-035"],
    "Diana Shepard": ["MAT-035", "CTI-115", "BAS-120", "CSC-121"],
    "Yoko Mayo": ["MAT-035"],
    "Rashad Ahmed": ["MAT-035", "BAS-120"],
    "Susan Jones": ["BAS-120", "CSC-121"]
}
# for each student in the statement dict, calc their total tuition
def display_all_tuition():
    for s in students:
        total_tuition = 0
        num_classes = 0
        print(f"{s} is taking classes {students[s]}") # students [s] is the list of classes for 
    # loop throught each students's classes
    
        for c in students[s]:
            print(c) # c is one class for one student
            for course in courses:
                #print(course)
                if c == course:
                    num_classes += 1
                    #print(courses[course]["tuition"])
                    student_tution = courses[course]['tuition']
                    total_tuition += student_tution
        print(f"{s}{num_classes}${total_tuition:.2f}")
        print("\n")
                


# Just an example to remind you how to pull data from a nested dictionary
# print(courses["MAT-035"]["desc"])

def display_course_list():
    print(f"{'Code':<15} {'Description':<30} {'Tuition':>10}")
    print("-" * 60)
    for course in courses:
        print(f"{course:<15} {courses[course]['desc']:<30} {courses[course]['tuition']:>10} ")

def lookup_course():
        code = input("Enter the course code: ")
        if code in courses:  
            print(f"\nCourse Code: {code}")
            print(f"Course Description: {courses[code]['desc']}")
            print(f"Tuition: ${courses[code]['tuition']:.2f}")
        else:
            print("\nCourse code not found.")



def display_specific_student():
    student_list = list(students.keys())
    ''''
    print(students["Zakari Watson"])
    print(students["Jerom Williams"])
    print(students["Dominique Ross"])
    print(students["Diana Shepard"])
    print(students["Yoko Mayo"])
    print(students["Rashad Ahmed"])
    print(students["Susan Jones"])
    '''
    for s, student in enumerate(students, start=1):  
        print(f"{s}) {student}")
    choice = int(input("Enter number that appears next to the student (1/2/3/4/5/7): "))
    if 1 <= choice <= len(student_list):
            student_name = student_list[choice - 1]
            student_courses = students[student_name]
            
            print(f"\nStudent: {student_name}")
            total_tuition = 0

            for course_code in student_courses:
                course_info = courses.get(course_code, {"desc": "Unknown Course", "tuition": 0})
                print(f"{course_code}: {course_info['desc']} - Tuition: ${course_info['tuition']:.2f}")
                total_tuition += course_info['tuition']
            
            print(f"\nTotal Tuition: ${total_tuition:.2f}")

    else:
            print("Invalid selection. Please choose a valid number.")



    

def display_num_of_students_tuition_for_all_courses():
     course_stats = {}
    
    # Initialize the dictionary with course codes and default values
     for course_code in courses:
        course_stats[course_code] = {
            "num_students": 0,
            "total_tuition": 0.0
        }
    
    # Count the number of students and calculate total tuition for each course
     for student in students:
        for course_code in students[student]:
            if course_code in course_stats:
                course_stats[course_code]["num_students"] += 1
                course_stats[course_code]["total_tuition"] += courses[course_code]["tuition"]
    
    
        print(f"{'Course Code':<15} {'Description':<30} {'# Students':>10} {'Total Tuition':>15}")
        print("-" * 70)
        for course_code, stats in course_stats.items():
            description = courses[course_code]["desc"]
            num_students = stats["num_students"]
            total_tuition = stats["total_tuition"]
            print(f"{course_code:<15} {description:<30} {num_students:>10} ${total_tuition:>14.2f}")

     





def menu():
    print("------------MENU-----------")
    print("1) Display Course Information")
    print("2) Lookup Course")
    print("3) Display Courses and Tuition for Specific Student")
    print("4) Display Tuition for All Students")
    print("5) Display # of Students and Tuition for All Courses")
    print("6) Exit")
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    if choice == '1':
        display_course_list()
    elif choice == '2':
        lookup_course()
    elif choice == '3':
         display_specific_student()
    elif choice == '4':
         display_all_tuition()
    elif choice == '5':
         display_num_of_students_tuition_for_all_courses()
    elif choice == '6':
         print("Program is exiting")
    
         















def main():
    menu()


if __name__ == "__main__":
        main()
    