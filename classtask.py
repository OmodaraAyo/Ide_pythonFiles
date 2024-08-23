def get_index(turple2):
        new_number = 0,0
        my_number = 0,0
        for i in range(len(turple2)):
            if i == 1:
                new_number = i, turple2[i][i]
            if i == 2:
                my_number = i, turple2[i][i]
        return new_number, my_number

turple2 = ("Orange", [10, 20, 30],(5, 15, 25))
result = get_index(turple2)
print(result)
