import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [rock, paper, scissors]
user_choice = int(input("What would you chose? 0 for rock , 1 for paper , 2 for scissors :   "))
if user_choice < 0 or user_choice > 2 :
    print("Invalid input ! you lose")
else :
    print(list[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose :")
    print(list[computer_choice])
    if computer_choice == 0 and user_choice == 2 :
        print("You lose")
    elif computer_choice == 2 and user_choice == 0 : 
        print("You win")
    elif user_choice > computer_choice : 
        print("You win")
    elif user_choice == computer_choice :
        print("Draw")
