d={"emp1":["sarvan","14.02.2004",85000],
"emp2":["sanjeev","12.12.2004",75000],
"emp3":["singar","12.01.2005",82000],
"emp4":["shanjay","16.9.2005",72000],
"emp5":["sugu","24.02.2005",60000],
"emp6":["aravind","3.4.2005",65000]}
print("the dictionary is :",d)
d["emp2"]=["kamesh","15.2.2004",100000]
print(d)
del d["emp4"]
print(d)
d.popitem()
print(d)
for i in d:
    d[i][2]=d[i][2]*1.05
print(d)


