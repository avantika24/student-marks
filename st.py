R1= [101, 102, 103, 104, 105,106]
s= ["Avani","Adi","Bahwna","Kriti","Gitti","Pihu"]
t=[97, 98, 89, 70, 60, 40]
roll=int(input("Eneter Roll Number of the Student:"))
if roll==R1[0]:
	print("Name:", s[0])
	print("Total Marks", t[0])
	print("Cngratulations! You are Pass")
	print
elif roll==R1[1]:
	print("Name:", s[1])
	print("Total Marks", t[1])
	print("Cngratulations! You are Pass")
elif roll==R1[2]:
	print("Name:", s[2])
	print("Total Marks", t[2])
	print("Cngratulations! You are Pass")
elif roll==R1[3]:
	print("Name:", s[3])
	print("Total Marks", t[3])
	print("Cngratulations! You are Pass")
elif roll==R1[4]:
	print("Name:", s[4])
	print("Total Marks", t[4])
	print("Cngratulations! You are Pass")
else:
	print("Sorry! you are fail")