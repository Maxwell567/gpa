#WAKAYE MAYAMBA MAXWELL
#BHU/19/04/05/0027
def gpa():
    name = str(input("what is your name? "))
    matric_number = str(input("what is your matric number? "))
    course_num = int(input("how many course did you apply? "))
    n = 0
    weighed_grade_point = 0
    total_credit_unit = 0
    x = 0


    for x in range(n, course_num):
        name_of_course = (input("Insert name of course "))

        course_unit_earned = int(input("couse unit earned for the course above "))
        grade = input("What was ur grade a,b,c,d,f? ")
        if grade == "a":
            weighed_grade_point += (course_unit_earned * 5)
            total_credit_unit += course_unit_earned
        elif grade == "b":
            weighed_grade_point += (course_unit_earned * 4)
            total_credit_unit += course_unit_earned
        elif grade == "c":
            weighed_grade_point += (course_unit_earned * 3)
            total_credit_unit += course_unit_earned
        elif grade == "d":
            weighed_grade_point += (course_unit_earned * 2)
            total_credit_unit += course_unit_earned
        elif grade == "f":
            weighed_grade_point += (course_unit_earned * 1)
            total_credit_unit += course_unit_earned
        else:
            print("Oops something went wrong!...Try again")
    gpa = weighed_grade_point/total_credit_unit
   # print(gpa)
    if (gpa >= 4.5) and (gpa <= 5.0):
        print(name)
        print(matric_number)
        print('Hurray ur a FIRST CLASS STUDENT ',gpa)
    elif (gpa >= 3.5) and (gpa <= 4.49):
        print(name)
        print(matric_number)
        print('seconnd CLASS upper STUDENT ',gpa)
    elif (gpa >= 2.5) and (gpa <= 3.49):
        print(name)
        print(matric_number)
        print('seconnd CLASS lower STUDENT ',gpa)
    elif (gpa >= 1.5) and (gpa <= 2.49):
        print(name)
        print(matric_number)
        print(' third CLASS STUDENT ',gpa)
    elif (gpa >= 0.0) and (gpa <= 1.49):
        print(name)
        print(matric_number)
        print('You failed ',gpa)
    else:
        print("Oops something went wrong!...Try again")

gpa()
