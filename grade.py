marks=int(input("Enter the marks of stuents"))
if marks >=90 and marks <=100:
    grade = "A+"
    print (f"Grade of students: {grade}");
elif marks >=80 and marks <=90:
    grade = "A"  
    print (f"Grade of students: {grade}");
elif marks >=70 and marks <=80:
    grade = "B" 
    print (f"Grade of students: {grade}");
elif marks>=60 and marks<=70:
    grade = "C"
    print (f"Grade of students: {grade}");
elif marks>=50 and marks<=60:
    grade = "D"
    print (f"Grade of students: {grade}");
else:
     grade = "fail"
     print (f"Grade of students: {grade}");


