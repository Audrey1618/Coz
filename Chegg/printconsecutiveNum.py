N = 24

for i in range(1, N + 1):
    if i % 5 == 0 and i % 3 == 0 and i % 2 == 0:
        print("CodilityTestCoders")
    elif i % 5 == 0 and i % 3 == 0:
        print("TestCoders")
    elif i % 5 == 0 and i % 2 == 0:
        print("CodilityCoders")
    elif i % 3 == 0 and i % 2 == 0:
        print("CodilityTest") 
    elif i % 5 == 0:
        print("Coders")  
    elif i % 3 == 0:
        print("Test")
    elif i % 2 == 0:
        print("Codility")
    else:
        print(i)
