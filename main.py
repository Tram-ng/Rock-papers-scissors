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

#Write your code below this line 👇
import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
computer_choice =  random.randint (0,2)
print (f"Computer chose {computer_choice}")
if computer_choice == 0 and user_choice == 2:
  print ("Computer win!")
elif user_choice == 0 and computer_choice == 2:
  print ("User win!")
elif user_choice > computer_choice:
  print("User win!")
elif computer_choice > user_choice:
  print ("Computer win!")
else : 
  print ("Tie")