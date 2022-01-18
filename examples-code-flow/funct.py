def intInput(prompt,default):
    try:
        return int(input(prompt))
    except:
        return default

age = intInput("How old is your car? ",0)
print("Your car is",age,"years old")

