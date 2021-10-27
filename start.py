# file for Exam 2
# Diego Gonzales
changeDigit(code)
number = list(code)
for i in range(4):
    for j in range(1, 4):
        number[i] = ((number[i]+1)%3)
        if j > 1:
            continue