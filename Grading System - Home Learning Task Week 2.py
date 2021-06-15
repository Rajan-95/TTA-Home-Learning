def grades():
    user = input('Please enter your name: ')
    print("Hi, " + user + "! Please have your exam score next to you. This program will calculate your percentage and grade.")
    examScore = int(input("Your recent maths exam was scored out of 75, how many marks did you get?"))
    # using while loop allows the user to re-enter exam score if they enter a value above 75
    while int(examScore) > 75: 
        print("Invalid exam score, the maximum marks on this paper were 75.")
        examScore = int(input("Please re-enter how many marks you scored: "))
    percentage = (examScore/75)*100
    # percentage variable converts the exam score into a % which allows us to break it down in to grading barriers
    if percentage >= 90 and percentage <= 100:
        grade = "A"
        # printing grade as a seperate value to use later in the program when comparing with target
        print("Amazing work! You scored " + str(percentage) + "%!. This is a grade " + grade)
    elif percentage >= 80 and percentage < 90:
        grade = "B"
        print("Well done, you scored " + str(percentage) + "%!. This is a grade " + grade)
    elif percentage >= 70 and percentage < 80:
        grade = "C"
        print("Well done, you scored " + str(percentage) + "%!. This is a grade " + grade)
    elif percentage >= 60 and percentage < 70:
        grade = "D"
        print("Well done, you scored " + str(percentage) + "%!. This is a grade " + grade)
    elif percentage >= 50 and percentage < 60:
        grade = "E"
        print("Well done, you scored " + str(percentage) + "%!. This is a grade " + grade)
    else:
        grade = "F"
        print("Unfortunately you received an " + grade + " on your maths exam which means you failed. The pass mark was 50%, please contact your tutor regarding a retake.")
    
    target = input("What was your target grade for this class?")
    # using while loop allows the user to re-enter their target grade if they put in a value that isn't between A-F
    # target.upper() will convert the user's input into a capital letter. Without this if user enters a lowercase grade, it loops back to asking them for their target again
    # with this feature, user can enter a lower case grade and automatically it will process as a capital letter without asking to re-enter 
    while target.upper() >= "G":
        # each letter has a value in python (ACSII), # A = 65, B = 66, C = 67, D = 68, E = 69, F = 70 << using this to determine whether target is greater than grade
        # In this scenario, grades only go from A-F hence if a value larger than F = 70, invalid message appears. Eg a letter further on in the alphabet than F
        print("Invalid target. Target grade must be between A-F. ")
        target = input("Please re-enter your target grade: ")
    if target.upper() > grade:
        # if target is greater than the grade, this means the letter provided for target (eg B, which equals 66 ) is greater than the actual grade (eg A, which = 65)
        # therefore displaying overachiever message, as the target grade is not a better grade than the actual grade the user achieved
        print("Wow! Well done, " + user + "! You smashed your target and over achieved on this exam! Great job!")
    elif target.upper() == grade:
        print("Well done, " + user + "! You are on target, keep it up!")
    else:  #target < grade: 
        # if target has a value less than grade, this means letter provided for target (eg B, which equals 66) is lower than the actual grade (eg D, which equals 68)
        # therefore displaying user underachieved as they didn't get a better grade than their target
        print("Unfortunately, you have under achieved on this exam. Please revise more thoroughly next time in order to achieve your target of grade " + target.upper())
    
grades()