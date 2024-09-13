def increment(numbers):
    for i in range(1,numbers+1):
        for j in range(1,i+1,+1):
            print(j, end=" ")
        print()
    return ""
print(increment(8))