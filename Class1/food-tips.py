# tips=int(input("Enter tip percentage: "))

choice=int(input("""
Select your choice:
1 - 15%
2 - 18%
3 - 20%
4 - type number
"""))

if tips == 1:
    print("standart")
elif tips == 2:
    print("Good")
elif tips == 3:
    print("Great")
elif tips > 4:
    tips=int(input("Enter tip percentage: "))
    if tip > 20:
        print("My hero")
    else:
        print("Provide right percentage")

else:
    print("Provide right percentage")