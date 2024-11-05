d={'chennai': 600028,'delhi':500028,'kolkatta':400028,'mumbai':300028}
city=input("enter the city : ")
if city not in d:
    print("city not found")
else:
    print(d[city])