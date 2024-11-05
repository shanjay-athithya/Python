while True:
    voltage=int(input("enter the number of voltage: "))
    if voltage ==5:
        print("active voltage")
    elif voltage<5:
        print("cut off voltage")
    else:
        print("break down voltage")
        break
