m=int(input("Marks in Maths: ")
s=int(input("Marks in Science: ")
e=int(input("Marks in English: ")
total_marks=m+e+s
average=total_marks/3
percentage=(total_marks/300)*100
grade=" "
if percentage>90:
      grade="A"
elif percentage>80 and percentage<=90:
    grade="B"
elif percentage>70 and percentage<=80:
    grade="c"
else:
    grade="Pass"
print(f"Total_marks: {total_marks}\nAverageMarks: {average}\nGrade: {grade}")
