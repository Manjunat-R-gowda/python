age=int(input("enter your age:"))
high_school_marks=int(input("enter your marks"))
entrence_exam=int(input("enter your entrence marks"))
if age <18:
	print("Too young for admission")
if age>=18 and high_school_marks>=70 and entrence_exam >=50:
	print("admission granted")
else:
	print("admmision died")
	
	


