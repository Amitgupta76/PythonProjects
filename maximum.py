student_marks = input("Input a list of student marks").split()
for n in range(0, len(student_marks)):
    student_marks[n] = int(student_marks[n])
print(student_marks)
max = 0

for i in student_marks:
    if(i>max):
        max = i
print(max)
        