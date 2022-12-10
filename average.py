student_heights = input("Input a list of student heights").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total = 0
for i in student_heights:
    total+=i
avg = total/(len(student_heights))
print(total)
print(avg)