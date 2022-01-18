proceed = True
while proceed:
    text = input("? ")
    if text == "s":
        print("SPACE")
    elif text == "e":
        proceed = False

print("We're done")