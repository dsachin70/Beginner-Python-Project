print("Welcome")

playing = input("Do you want to play?  ")

if playing.lower()!= "yes":
    quit()

print("okay ! Let's play :)")
score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect!")

answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct")
    score += 1

else:
    print("incorrect!")

answer = input("what does RAM stand for? ")
if answer.lower() == "random accesis memory":
    print("correct")
    score += 1

else:
    print("incorrect!")

answer = input("what does GUI stand for? ")
if answer.lower() == "graphical user interface":
    print("correct")
    score += 1
else:
    print("incorrect!")

answer = input("what does ROM stand for? ")
if answer.lower() == "read only memory":
    print("correct")
    score += 1
else:
    print("incorrect!")

print("You got " + str(score) + "quations correct!")
print("You got" + str((score/5) * 100 ) + "%.")