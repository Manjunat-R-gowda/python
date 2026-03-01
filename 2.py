temp=int(input("enter a temperature"))
if temp<10:
	print("cold")
elif temp>=10 and temp<=30:
	print("warm")
elif temp>30:
	print("hot")
	
	year=int(input("enter a year :"))
if year % 4==0 and (year%100!=0 or  year %400==0):
	print('leap year')
else:
	print("not a leap year")