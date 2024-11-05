BP=int(input("enter the base pay: "))
DA=88*BP/100
HRA=8*BP/100
CCA=1000
Insurance=2000
PF=10*BP/100
GrossPay=BP+DA+HRA+CCA
Deductions=Insurance+PF
netsalary=GrossPay-Deductions
print("the net salary is: ",netsalary)
