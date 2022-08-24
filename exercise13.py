
#Task 1

for i in range(2):
    phrase = str(input("Input a Phrase: "))
    print(phrase)
    if (len(phrase) %2) != 0:
        print(phrase + " " +"is odd")
    else:
        print(phrase + " " + "is even")