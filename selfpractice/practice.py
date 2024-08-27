number_Of_Student, number_Of_Subject = 4, 2
student_And_Their_Score_list = [[0 for _ in range(number_Of_Subject)] for _ in range(number_Of_Student)]
for i in range(number_Of_Student):
    for j in range(number_Of_Subject):
        score = int(input("Enter score: "))
        student_And_Their_Score_list[i][j] = score
print(student_And_Their_Score_list)