from statistics import mean


# Declare and Defne list and Dict
subjects  = ["Bangla", "English", "Math", "Science"]
scores = {}


# Calculate result
def calculate_result(sub_and_score):
    average = round(mean([score for score in sub_and_score.values()]),2)

    if average > 90:
        print("Your Grade is: A+")
    elif average > 80:
        print("Your Grade is: A")
    elif average > 70:
        print("Your Grade is: B")
    elif average > 60:
        print("Your Grade is: C")
    elif average > 40:
        print("Your Grade is: D")
    else:
        print("Your Grade is: F")



#Taking Input for All Subjects
def taking_student_score():
    for subject in subjects:
        score = - 1
        validator = True
        while validator:
            try:
                score = float(input(f"Enter Score for {subject}: "))  # Take score input based on subject
                if not 0 < score < 101:
                    raise TypeError("Number Must be within 0-100")

                scores[subject] = score
                validator = False
            except TypeError as e:
                print(e)
            except ValueError as e:
                print(f"Please Input Numerical Value. {score} is not a Number")

# Take scores by user and store in the List
taking_student_score()

# Separator
print()

# Calculate Result and Show result based on average
calculate_result(scores)

