age = -1

while age < 0:
    age = int(input("How old is your car? "))

if age < 10 :
    print("So, not an oldtimer yet...")
elif age < 15:
    print("On its way to become an oldtimer...")
else:
    print("I'm impressed you kept it alive so long...")
