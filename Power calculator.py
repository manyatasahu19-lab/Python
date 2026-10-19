base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
result = 1
print("\nCalculating the power")
print("------------------------")
for i in range(exponent):
    result = result * base
    print("Step",i + 1,":",result)
    print("--------------------------------")
    print("base:",base)
    print("exponent:",exponent)
    print("Final answer:",result)
    print("Power expression:",base,"^",exponent)
    print("====================================")
    print("        CALCULATION COMPLETE           ")
    print("======================================")