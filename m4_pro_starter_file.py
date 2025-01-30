courses = {
    "MAT-035": {"desc": "Concepts of Algebra", "tuition": 460},
    "CTI-115": {"desc": "Computer System Foundations", "tuition": 520.98},
    "BAS-120": {"desc": "Intro to Analytics", "tuition": 500},
    "CSC-121": {"desc": "Python Programming", "tuition": 783.88}
}

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
                    student_tution = courses[course]['tuitions']
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
















def main():
    menu()


if __name__ == "__main__":
        main()
    