import random
print("~~~~~~~~~~~~Welcome to AZ GAMEING~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~Welcome to RPS~~~~~~~~~~~~~~")

user_score = 0
comp_score = 0
ties = 0

name = input('ENTERN YOUR NAME HERE : ')
print('''Winning rules:
      1. rock vs paper = paper
      2. paper vs scissore = scissore
      3. rock vs scissore = rock''')

print('''choices are:
1. rock
2. paper
3. scissore
''')
while True:
    choice = int(input('enter a input 1-3 : '))

    while choice > 3 or choice< 1 :
        choice =int(input('enter a valid numher = '))

    if choice == 1:
        user_choice = 'rock'
    elif choice == 2:
        user_choice = 'paper'
    else:
        user_choice = 'scissore'

    print('user_choice is ', user_choice )
    print( )
    print("now it is computer's turn ")

    computer = random.randint(1,3)

    if computer == 1:
        comp_choice = 'rock'
    elif computer == 2:
        comp_choice = 'paper'
    else:
        comp_choice = 'scissore'

    print("The computer's choice is ", comp_choice )
    print( )

    if ((user_choice == 'paper' and comp_choice == 'rock') or (user_choice =="rock" and comp_choice == 'paper')):
        print('wins paper')
        result = 'paper'

    elif ((user_choice == 'scissore' and comp_choice == 'rock') or (user_choice =="rock" and comp_choice == 'scissore')):
        print('wins rock')
        result = "rock"

    elif (comp_choice == user_choice):
        print("it's a tie")
        result = "tie"
    else:
        print('wins scissore')
        result = 'scissore'

    if result == "tie" :
        ties +=1
    elif result == user_choice:
        print("that user a wins")
        user_score +=1
    else:
        print("that computer's a wins")
        comp_score +=1

    print()
    print(name)
    print('a user score is',user_score )
    print("a computer's score is",comp_score )
    print("a tie score is ", ties)

    repeat = input("do you want to play again ?")
    if repeat == "no" or repeat == 'NO' or repeat == 'No' or repeat == 'nO':
        break
    print("GAME OVER ")
