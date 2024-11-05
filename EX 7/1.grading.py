def assign_grade(marks):    
    if marks>=90:
        return "A"
    elif 90>marks>=80:
        return "B"
    elif 80>marks>65:
        return "C"
    elif 65>=marks>=40:
        return "D"
    elif marks<40:
        return "F"
l=[]
for i in range (1,6):
    marks=int(input("enter english mark of student :"))
    l.append(assign_grade(marks))
print(l)
