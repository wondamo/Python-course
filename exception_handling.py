def ageInSeconds(age):
    return (age * 12 * 30)

try:
    var = int(input("How old are you? "))
    print(ageInSeconds(var))
except:
    print("You did not enter a number")
finally:
    print("Thank you")