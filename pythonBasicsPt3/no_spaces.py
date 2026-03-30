sentance = input("enter the sentence: ")
blanck = 0
for word in sentance:
    if word == " ":
        blanck += 1

print("the number of blanks: ", blanck)
