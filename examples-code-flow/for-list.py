ages = [1,3,5,8,12,16,20]

for age in ages:
    print("Car is ",age,"years old")

    if age < 10 :
        print("So, not an oldtimer yet...")
    elif age < 15:
        print("On its way to become an oldtimer...")
    else:
        print("I'm impressed you kept it alive so long...")
        