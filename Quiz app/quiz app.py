#Fun General Knowledge Quiz

questions = ("1. Which animal is known as the 'Ship of the Desert'",
             "How many days are there in a week?",
             " How many hours are there in a day?",
             "How many letters are there in the English alphabet?",
             " Rainbow consist of how many colours?",
             "How many days are there in a year?",
             "How many minutes are there in an hour?",
             "How many seconds are there in a minute?",
             "How many seconds make one hour?",
             "Which animal is known as the king of the jungle?")

options =  (("A. Camel","B. Cat", "C. Dog","D.  B and C Both"),
            ("A.  9 days","B.  7 days","C.  5 days","D. B and C Both"),
            ("A.  21 hours","B.  29 hours","C.  24 hours","D. None of these above"),
            ("A.  30 letters","B.  21 letters","C.  22 letters","D.  26 letters"),
            ("A.  9 colours" ,"B.  4 colours" ,"C.  7 colours","D. All of the above"),
            ("A. 361 days","B. 365 days (not a leap year)","C. 361 days","D. None of these"),
            ("A. 60 minutes","B. 90 minutes","C. 63 minutes","D. None of these"),
            ("A. 60 seconds","B. 65 seconds","C. 70 seconds","D. 90 seconds"),
            ("A. 3600 seconds","B. 4600 seconds","C. 3900 seconds","D. All of the above"),
            ("A. Elefanten","B. Tiger","C. Loin","D. Jaguar"))

answers = ("A", "B", "C", "D", "C", "B", "A", "A", "A", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)


    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1


print("<<<<<RESULT>>>>>")


print("answers: ",end=" ")
for answer in answers:
    print(answer,end=" ")
print()


print("gussess: ",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")