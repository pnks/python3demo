try:
    age = int(input("How old is your car? "))
except Exception as x:
    print("ERROR:",x)
    age = 0

print("Your car is",age,"years old")
