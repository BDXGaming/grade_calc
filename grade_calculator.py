DEFAULT_LETTER_GRADES = {93:"A",90:"A-", 87:"B+", 83:"B", 80:"B-", 77:"C+",73:"C",70:"C-", 67:"D", 63:"D",60:"D", 0:"F"}
LETTER_GRADE_TO_GPA = {"A":4.0, "A-":3.67, "B+":3.33, "B":3.0, "B-":2.67, "C+":2.33, "C":2.00, "C-":1.67, "D+":1.33, "D":1.0, "F":0}


def is_valid_number(number):
    """
    Checks if the number given is a valid number (i.e. can be converted into a float)
    :param number: The number to check if valid
    :return bool: The boolean result of whether or not the number is valid
    """

    valid_chars = ['0','1', '2', '3', '4','5','6','7','8','9','.']  

    for char in list(str(number)):
        if char not in valid_chars:
            return False

    return True


def percent_to_letter_grade(grade_percent, use_default=True, custom_grading_scale = {}):
    """
    This function converts the percet grade to a letter grade.
    :param grade_percent: The grade percentage to be converted to a letter grade.
    :return letter_grade: The letter grade which represents the percentage grade.
    """

    letter_grade = "F" # The default letter grade (F)

    # If the default grading scale should be used, set the params to the default
    if use_default:
        letter_grades = DEFAULT_LETTER_GRADES
        grade_scale = list(DEFAULT_LETTER_GRADES.keys())
        grade_scale.reverse()

    # Use the custom grading scale provided in function invokation
    else:
        letter_grades = custom_grading_scale
        grade_scale = list(custom_grading_scale.keys())
        grade_scale.reverse()

    # Iterates over all percentages and finds the letter grade for the given percentage
    for percent in grade_scale:
        if percent <= grade_percent:
            letter_grade = letter_grades[percent]

    # Returns the letter grade
    return letter_grade


def collect_percent_grade_inputs(number_of_grades: int):
    """
    This method collects all grades for the given number of courses provided.
    :param number_of_grades: The number of courses for which grades should be collected.
    :return grades: A dictionary object which maps coursename to letter grade
    """

    grades = {} # The keys are the coursename and the values are the grade percentages 
    i = 0

    while(i<number_of_grades):

        course = input("Enter a coursename: ")
        credits = input("Enter the number of credits for the course: ")
        grade = input(f"Enter a grade percentage for {course}: ")

        if is_valid_number(grade):
            i+=1
            grade = percent_to_letter_grade(float(grade))
            grades[course] = {"letter_grade":grade, "gpa":LETTER_GRADE_TO_GPA[grade], "credits":int(credits)}

        else:
            print("That input is not valid.")
    
    return grades


def calculate_gpa(grade_info):

    total_gpa_points = 0
    total_credits = 0

    for course, grade in grade_info.items():
        gpa_points = grade['gpa'] * grade['credits']
        total_credits += grade['credits']
        total_gpa_points += gpa_points

    return total_gpa_points/total_credits


if __name__ == "__main__":
    number_of_grades = input("Enter the number of courses which you want to enter a grade for: ")
    print(f"Your GPA is: {calculate_gpa(collect_percent_grade_inputs(int(number_of_grades)))}")

