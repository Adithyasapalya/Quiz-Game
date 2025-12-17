print("Welcome to the Quiz Game!")

playing = input("Do you want to play? (yes/no): ")

if playing != "yes":
    quit()
print("okay! lets play :)")   

answer= input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")