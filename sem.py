d={1:{"shan":12,"sar":13},2:{"san":14,"ara":15}}
"""for k,v in d.items():
    print("s no: ",k)
    for key in v:
        print(key+":",v[key])
print(d.pop())"""
d1={3:{"vin":16,"sin":19}}
d3={"shan":12,"sar":19,"san":11,"ara":15}
d.update(d1)
print(sorted(d3.items(),key=lambda x: x[0]))