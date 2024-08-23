number_Of_Student = int(input("Enter number of students: "))
number_Of_Subject = int(input("Enter number subject: "))

student_Scores_list = [[0 for _ in range(number_Of_Student)] for _ in range(number_Of_Subject)]
score_Total = []
sum_Of_All_Scores = 0
for counter in range(number_Of_Student):
    each_Student_Score = 0
    print("")
    print(f"Student: {counter + 1}")
    for count in range(number_Of_Subject):
        while True:
            try:
                subject_Scores = int(input(f"Enter score for subject {count + 1}: "))
                if(subject_Scores > 0 and subject_Scores <= 100):
                    student_Scores_list[counter][count] = subject_Scores
                    each_Student_Score = each_Student_Score + subject_Scores
                    sum_Of_All_Scores = sum_Of_All_Scores + subject_Scores
                    break
                else:
                    print("invalid input: Enter score between 0 and 100")
            except ValueError:
                print("invalid input: Enter score between 0 and 100")
    score_Total.append(each_Student_Score)
#print(student_Scores_list)
#print(score_Total)
print("STUDENTS")
for index in range(number_Of_Student):
    print("Student" + str(index + 1) + ":")
